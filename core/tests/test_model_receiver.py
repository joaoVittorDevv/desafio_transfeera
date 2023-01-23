import unittest
from ..models.model_bank import Bank, Agency, Account
from django.test import TestCase

from ..models.model_receiver import Receiver


class ReceiverModelTest(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Bank Test")
        self.agency = Agency.objects.create(agency_number=12345, from_bank=self.bank)
        self.account = Account.objects.create(account_number=54321, account_type="C", from_agency=self.agency)
        self.receiver = Receiver.objects.create(
            name="Joao", cpf_cnpj='171.104.950-60',
            status="V", email="joao@example.com",
            key_type="CPF", key="123456789")
        self.receiver.account.add(self.account)

    def test_name_label(self):
        receiver = Receiver.objects.get(name="Joao")
        field_label = receiver._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Nome')

    def test_cpf_cnpj_validators(self):
        receiver = Receiver.objects.get(name="Joao")
        self.assertEquals(receiver.cpf_cnpj, '171.104.950-60')

    def test_status_choices(self):
        receiver = Receiver.objects.get(name="Joao")
        self.assertEquals(receiver.status, "V")
        self.assertEquals(receiver.get_status_display(), "Validado")

    def test_key_type_choices(self):
        receiver = Receiver.objects.get(name="Joao")
        self.assertEquals(receiver.key_type, "CPF")
        self.assertEquals(receiver.get_key_type_display(), "CPF")

    def test_account_field(self):
        receiver = Receiver.objects.get(name="Joao")
        self.assertEquals(receiver.account.get(id=self.account.id), self.account)