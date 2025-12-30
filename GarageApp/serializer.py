from rest_framework import serializers
from GarageApp.models import Customer,Service

class CustomerSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model= Customer
        fields="__all__"

class ServiceSerialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    customer=CustomerSerialiser(read_only=True)
    class Meta:
        model= Service
        fields="__all__"