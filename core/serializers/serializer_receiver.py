from rest_framework import serializers
from ..validations.validations_receiver import validate_pix_key
from ..models.model_receiver import Receiver
from django.core.exceptions import ValidationError


class ReceiverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receiver
        fields = '__all__'

    def create(self, validated_data, pk=None):
        if validate_pix_key(validated_data['key_type'], validated_data['key']) is not None:
            receiver = Receiver.objects.create(
                name=validated_data['name'],
                cpf_cnpj=validated_data['cpf_cnpj'],
                status=validated_data['status'],
                email=validated_data['email'],
                key_type=validated_data['key_type'],
                key=validated_data['key'],

            )
            for account in validated_data['account']:
                receiver.account.add(account)

            return receiver
        else:
            raise ValidationError('Dados da chave pix inválidos')

    def update(self, instance, validated_data):

        receiver_update = Receiver.objects.get(id=instance.id)
        if receiver_update.status == 'V':
            receiver_update.email = validated_data['email']
            receiver_update.save()
        else:
            receiver_update.name = validated_data['name']
            receiver_update.cpf_cnpj = validated_data['cpf_cnpj']
            receiver_update.status = validated_data['status']
            receiver_update.email = validated_data['email']
            receiver_update.key_type = validated_data['key_type']
            receiver_update.key = validated_data['key']
            receiver_update.account.set(validated_data['account'])
            receiver_update.save()
        return receiver_update

