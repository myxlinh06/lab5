from rest_framework import serializers
from .models import OrdersReport, ProductReport

class OrdersReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersReport
        fields = '__all__'

class ProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReport
        fields = '__all__'
