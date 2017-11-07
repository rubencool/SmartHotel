from django.conf.urls import url
from django.contrib import admin

from .views import (
	CustomerCreateAPIView,
	CustomerListAPIView,
	CustomerDetailAPIView,
	CustomerUpdateAPIView,
	CustomerDeleteAPIView,
	CustomerTableAPIView,

	#order
    OrderCreateAPIView,
   	OrderListAPIView,
   	OrderDetailAPIView,
   	OrderUpdateAPIView,
   	OrderDeleteAPIView,
   	OrderCustomerAPIView,
)


urlpatterns = [
	url(r'^create$', CustomerCreateAPIView.as_view(), name='customer-create'),
	url(r'^$', CustomerListAPIView.as_view(), name='customer-list'),
	url(r'^(?P<pk>\d+)/$', CustomerDetailAPIView.as_view(), name='customer-detail'),
	url(r'^(?P<pk>\d+)/edit/$', CustomerUpdateAPIView.as_view(), name='customer-update'),
	url(r'^(?P<pk>\d+)/delete/$', CustomerDeleteAPIView.as_view(), name='customer-delete'),
	url(r'^table/(?P<table_id>\d+)$', CustomerTableAPIView.as_view(), name='which-table-query'),


# order
	url(r'^order/create$', OrderCreateAPIView.as_view(), name='order-create'),
	url(r'^order$', OrderListAPIView.as_view(), name='order-list'),
	url(r'^order/(?P<pk>\d+)/$', OrderDetailAPIView.as_view(), name='order-detail'),
	url(r'^order/(?P<pk>\d+)/edit/$', OrderUpdateAPIView.as_view(), name='order-update'),
	url(r'^order/(?P<pk>\d+)/delete/$', OrderDeleteAPIView.as_view(), name='order-delete'),
	url(r'^order/customer/(?P<cust_id>\d+)$', OrderCustomerAPIView.as_view(), name='which-customer-query'),

]