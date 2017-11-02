from rest_framework.serializers import ModelSerializer

from food.models import (
	Category,
	Order,
	Item,
	Table
)

class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'

class ItemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'

class CategoryCreateSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'cat_name'
		]

class TableSerializer(ModelSerializer):
	class Meta:
		model = Table
		fields = '__all__'