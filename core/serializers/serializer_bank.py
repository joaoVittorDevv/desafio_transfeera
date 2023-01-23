from rest_framework import serializers

from ..models.model_bank import Bank, Agency, Account


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'



class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
