import unittest

from rest_framework.exceptions import ValidationError

from ..models.model_receiver import Receiver
from ..serializers.serializer_receiver import ReceiverSerializer
from ..models.model_bank import Bank, Agency, Account
from ..validations.validations_receiver import validate_pix_key

class ReceiverSerializerTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Bank Test")
        self.agency = Agency.objects.create(agency_number=12345, from_bank=self.bank)
        self.account = Account.objects.create(account_number=54321, account_type="C", from_agency=self.agency)
        self.receiver = Receiver.objects.create(name='Joao', cpf_cnpj=12345678912, status='V', email='joao@example.com',
                                            key_type='CPF', key='123.456.789-12')
        self.receiver.account.add(self.account)

    def test_create(self):
        validated_data = {
            'name': 'Joao',
            'cpf_cnpj': '12345678912',
            'status': 'V',
            'email': 'joao@example.com.com',
            'key_type': 'CPF',
            'key': '123.456.789-12',
            'account': self.account
        }

        receiver = Receiver.objects.create(
            name=validated_data['name'],
            cpf_cnpj=validated_data['cpf_cnpj'],
            status=validated_data['status'],
            email=validated_data['email'],
            key_type=validated_data['key_type'],
            key=validated_data['key'],
        )
        receiver.account.add(validated_data['account'])

        self.assertEqual(receiver.name, validated_data['name'])
        self.assertEqual(receiver.cpf_cnpj, validated_data['cpf_cnpj'])
        self.assertEqual(receiver.status, validated_data['status'])
        self.assertEqual(receiver.email, validated_data['email'])
        self.assertEqual(receiver.key_type, validated_data['key_type'])
        self.assertEqual(receiver.key, validated_data['key'])
        self.assertEqual(receiver.account.get(id=self.account.id), validated_data['account'])

    def test_validate_pix_key(self):
        validated_data = {
            'key_type': 'CPF',
            'key': '123.456.789-12'
        }
        self.assertIsNotNone(validate_pix_key(validated_data['key_type'], validated_data['key']))

    def test_update(self):
        validated_data = {
            'name': 'Joao',
            'cpf_cnpj': '12345678912',
            'status': 'V',
            'email': 'joao@example.com',
            'key_type': 'CPF',
            'key': '123.456.789-12',
            'account': self.account
        }

        receiver_update = ReceiverSerializer(data=validated_data)
        receiver_update.update(self.receiver, validated_data)

        self.assertEqual(self.receiver.name, 'Joao')
        self.assertEqual(self.receiver.cpf_cnpj, 12345678912)
        self.assertEqual(self.receiver.status, 'V')
        self.assertEqual(self.receiver.email, 'joao@example.com')
        self.assertEqual(self.receiver.key_type, 'CPF')
        self.assertEqual(self.receiver.key, '123.456.789-12',)
        self.assertEqual(self.receiver.account.get(id=self.account.id), self.account)
