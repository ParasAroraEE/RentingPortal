from django.shortcuts import render
from address.models import Address
from address.serializers import AddressSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = AddressSerializer

    def get_queryset(self):

        try:
            return Address.objects.all()
        except Exception as err:
            return {}
