import unittest
from ..models.model_bank import Bank, Agency, Account


class TestBankModel(unittest.TestCase):

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Bank Test")
        self.agency = Agency.objects.create(agency_number=12345, from_bank=self.bank)
        self.account = Account.objects.create(account_number=54321, account_type="C", from_agency=self.agency)

    def test_bank_name(self):
        self.assertEqual(self.bank.bank_name, "Bank Test")

    def test_agency_number(self):
        self.assertEqual(self.agency.agency_number, 12345)

    def test_account_number(self):
        self.assertEqual(self.account.account_number, 54321)

    def test_account_type(self):
        self.assertEqual(self.account.account_type, "C")
