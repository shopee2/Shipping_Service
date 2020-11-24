from rest_framework import serializers
from .models import *

class OrderDescriptionSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.CharField(source="get_status_display")
    class Meta:
        model = OrderDescription
        fields = '__all__'
        read_only_fields = ['id']

class CarrierSerializer(serializers.ModelSerializer):
    estimated = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Carrier
        fields = '__all__'
        read_only_fields = ['id']

class CarrierNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['name']
        read_only_fields = ['id']

class OrderItemSerializer(serializers.ModelSerializer):
    carrier = CarrierNameSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'