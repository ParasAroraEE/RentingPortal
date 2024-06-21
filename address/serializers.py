
from rest_framework import serializers
from address.models import Address
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = '__all__'
        # fields = ['id', 'name']
