import unittest
from django.test import TestCase
from ..serializers.serializer_bank import BankSerializer, AgencySerializer, AccountSerializer
from ..models.model_bank import Bank, Agency, Account

class TestSerializers(TestCase):

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.agency = Agency.objects.create(agency_number="12345", from_bank=self.bank)
        self.account = Account.objects.create(account_number="54321", account_type="C", from_agency=self.agency)

    def test_bank_serializer(self):
        serializer = BankSerializer(instance=self.bank)
        data = serializer.data
        self.assertEqual(data["bank_name"], "Test Bank")

    def test_agency_serializer(self):
        serializer = AgencySerializer(instance=self.agency)
        data = serializer.data
        self.assertEqual(data["agency_number"], 12345)
        self.assertEqual(data["from_bank"], self.bank.id)

    def test_account_serializer(self):
        serializer = AccountSerializer(instance=self.account)
        data = serializer.data
        self.assertEqual(data["account_number"], 54321)
        self.assertEqual(data["account_type"], "C")
        self.assertEqual(data["from_agency"], self.agency.id)
