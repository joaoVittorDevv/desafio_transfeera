from rest_framework.test import APIClient
from unittest import TestCase
from ..viewsets.viewset_receiver import ReceiverViewSet, DjangoFilterBackend
from ..serializers.serializer_receiver import ReceiverSerializer
from ..models.model_receiver import STATUS_CHOICES, PIX_KEY_CHOICES, Receiver
from ..models.model_bank import Bank, Agency, Account

class ReceiverViewSetTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.bank = Bank.objects.create(bank_name="Bank Test")
        self.agency = Agency.objects.create(agency_number=12345, from_bank=self.bank)
        self.account = Account.objects.create(account_number=54321, account_type="C", from_agency=self.agency)
        self.receiver = Receiver.objects.create(
            name="Joao", cpf_cnpj='171.104.950-60',
            status="V", email="joao@example.com",
            key_type="CPF", key="123.456.789-12")
        self.receiver.account.add(self.account)

    def test_STATUS_CHOICES_validity(self):

        self.assertIn(('V', 'Validado'), STATUS_CHOICES)
        self.assertIn(('R', 'Rascunho'), STATUS_CHOICES)

    def test_PIX_KEY_CHOICES_validity(self):

        self.assertIn(('PHONE', 'Telefone'), PIX_KEY_CHOICES)
        self.assertIn(('CPF', 'CPF'), PIX_KEY_CHOICES)
        self.assertIn(('CNPJ', 'CNPJ'), PIX_KEY_CHOICES)
        self.assertIn(('EMAIL', 'Email'), PIX_KEY_CHOICES)
        self.assertIn(('ALKEY', 'Chave Aleatória'), PIX_KEY_CHOICES)

    def test_ReceiverViewSet_queryset(self):
        self.assertEqual(type(ReceiverViewSet.queryset), type(Receiver.objects.all()))

    def test_ReceiverViewSet_serializer_class(self):
        self.assertEqual(ReceiverViewSet.serializer_class, ReceiverSerializer)

    def test_ReceiverViewSet_filter_backends(self):
        self.assertEqual(ReceiverViewSet.filter_backends, [DjangoFilterBackend])

    def test_ReceiverViewSet_filterset_fields(self):
        self.assertEqual(ReceiverViewSet.filterset_fields, ['name', 'status', 'key_type', 'key'])

    def test_get(self):
        request = self.client.get('/receiver/')
        self.assertEqual(request.status_code, 200)

    def test_post(self):
        request = self.client.post(
            '/receiver/',
            {
                'name': 'Joao',
                'cpf_cnpj': '17110495070',
                'status': 'V',
                'email': 'joao@example.com',
                'key_type': 'CPF',
                'key': '123.456.789-12',
                'account': [self.account.id],
            },
            format='json'
            )

        self.assertEqual(request.status_code, 201)

    def test_put(self):

        request = self.client.put(
            f'/receiver/{self.receiver.id}/',
            {
                'name': 'Joao vittor',
                'cpf_cnpj': '17110495070',
                'status': 'R',
                'email': 'joaovittor@example.com',
                'key_type': 'CPF',
                'key': '132.456.789-13',
                'account': [self.account.id],
            },
            format='json'
            )

        self.assertEqual(request.status_code, 200)

    def test_delete(self):

        request = self.client.delete(
            f'/receiver/{self.receiver.id}/')

        self.assertEqual(request.status_code, 204)
