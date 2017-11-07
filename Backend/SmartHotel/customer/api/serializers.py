from rest_framework.serializers import ModelSerializer

from customer.models import (
	Customer,
	Order
)

class CustomerSerializer(ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'

class OrderCustomerSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = ('item','quantity','rate','total')