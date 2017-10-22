from rest_framework.generics import (
	CreateAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView	
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from food.models import Category, Item, Order

from .permissions import IsOwnerOrReadOnly

from .serializers import (
	CategorySerializer,
	CategoryCreateSerializer,
	ItemSerializer, OrderSerializer)

class CategoryCreateAPIView(CreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryCreateSerializer
	permission_classes = [IsAdminUser]

class CategoryListAPIView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = [IsAdminUser,IsOwnerOrReadOnly]

class CategoryDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	# item
class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	permission_classes = [IsAdminUser]

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	permission_classes = [IsAdminUser,IsOwnerOrReadOnly]

class ItemDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

# Order
class OrderCreateAPIView(CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAdminUser]

class OrderListAPIView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAdminUser]

class OrderDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer