from rest_framework import viewsets
from ..models.model_bank import Bank, Agency, Account
from ..serializers.serializer_bank import BankSerializer, AgencySerializer, AccountSerializer


class BankViewSet(viewsets.ModelViewSet):

    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AgencyViewSet(viewsets.ModelViewSet):

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
