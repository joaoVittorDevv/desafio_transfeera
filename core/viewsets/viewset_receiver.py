from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ..models.model_receiver import Receiver
from ..serializers.serializer_receiver import ReceiverSerializer

class ReceiverViewSet(viewsets.ModelViewSet):

    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'status', 'key_type', 'key']

