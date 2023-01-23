import unittest
from ..models.model_bank import Bank, Agency, Account
from rest_framework.test import APIClient


class TestBankAgencyAccountModels(unittest.TestCase):

    def setUp(self):

        self.client = APIClient()

        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.agency = Agency.objects.create(agency_number=123, from_bank=self.bank)
        self.account = Account.objects.create(account_number=12345,
                                                account_type="C",
                                                from_agency=self.agency)

    def test_bank_created_at_field(self):
        self.assertIsNotNone(self.bank.created_at)

    def test_agency_created_at_field(self):
        self.assertIsNotNone(self.agency.created_at)

    def test_account_created_at_field(self):
        self.assertIsNotNone(self.account.created_at)

    def test_get_bank(self):
        request = self.client.get('/bank/')
        self.assertEqual(request.status_code, 200)

    def test_post_bank(self):
        request = self.client.post(
            '/bank/',
            {
                'bank_name': 'Bank',
            },
            format='json'
            )

        self.assertEqual(request.status_code, 201)

    def test_put_bank(self):

        request = self.client.put(
            f'/bank/{self.bank.id}/',
            {
                'bank_name': 'banco',

            },
            format='json'
            )

        self.assertEqual(request.status_code, 200)

    def test_delete_bank(self):

        request = self.client.delete(
            f'/bank/{self.bank.id}/')

        self.assertEqual(request.status_code, 204)

    def test_get_agency(self):
        request = self.client.get('/agency/')
        self.assertEqual(request.status_code, 200)

    def test_post_agency(self):
        request = self.client.post(
            '/agency/',
            {
                'agency_number': 645546,
                'from_bank': self.bank.id
            },
            format='json'
            )

        self.assertEqual(request.status_code, 201)

    def test_put_agency(self):

        request = self.client.put(
            f'/agency/{self.agency.id}/',
            {
                'agency_number': 645546,
                'from_bank': self.bank.id

            },
            format='json'
            )

        self.assertEqual(request.status_code, 200)

    def test_delete_agency(self):

        request = self.client.delete(
            f'/agency/{self.agency.id}/')

        self.assertEqual(request.status_code, 204)

    def test_get_account(self):

        request = self.client.get('/account/')
        self.assertEqual(request.status_code, 200)

    def test_post_account(self):
        request = self.client.post(
            '/account/',
            {
                'account_number': 564654,
                'account_type': 'C',
                'from_agency': self.agency.id
            },
            format='json'
            )

        self.assertEqual(request.status_code, 201)

    def test_put_account(self):

        request = self.client.put(
            f'/account/{self.account.id}/',
            {
                'account_number': 798978,
                'account_type': 'C',
                'from_agency': self.agency.id

            },
            format='json'
            )

        self.assertEqual(request.status_code, 200)

    def test_delete_account(self):

        request = self.client.delete(
            f'/account/{self.account.id}/')

        self.assertEqual(request.status_code, 204)
