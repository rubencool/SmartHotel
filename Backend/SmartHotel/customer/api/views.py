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

from customer.models import Customer, Order
from django.shortcuts import get_object_or_404


from .permissions import IsOwnerOrReadOnly

from .serializers import (
	CustomerSerializer,
	OrderSerializer,
	OrderCustomerSerializer,
	)

class CustomerCreateAPIView(CreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerListAPIView(ListAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class CustomerDetailAPIView(RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerTableAPIView(ListAPIView):
	#queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_field = 'table_id'
	def get_queryset(self):
	    table_id = self.kwargs["table_id"]
	    return Customer.objects.filter(table_id=table_id)

# Order
class OrderCreateAPIView(CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

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

class OrderCustomerAPIView(ListAPIView):
	#queryset = Customer.objects.all()
	serializer_class = OrderCustomerSerializer
	lookup_field = 'cust_id'
	def get_queryset(self):
	    cust_id = self.kwargs["cust_id"]
	    return Order.objects.filter(cust_id=cust_id)
