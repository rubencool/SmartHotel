from django.conf.urls import url
from django.contrib import admin

from .views import (
	CategoryCreateAPIView,
	CategoryListAPIView,
	CategoryDetailAPIView,
	CategoryUpdateAPIView,
	CategoryDeleteAPIView,

	# item
	ItemCreateAPIView,
	ItemListAPIView,
	ItemDetailAPIView,
	ItemUpdateAPIView,
	ItemDeleteAPIView,

	#order
	OrderCreateAPIView,
	OrderListAPIView,
	OrderDetailAPIView,
	OrderUpdateAPIView,
	OrderDeleteAPIView,

	#order
    TableCreateAPIView,
   	TableListAPIView,
   	TableDetailAPIView,
   	TableUpdateAPIView,
   	TableDeleteAPIView
)


urlpatterns = [
	url(r'^category/create$', CategoryCreateAPIView.as_view(), name='category-create'),
	url(r'^category$', CategoryListAPIView.as_view(), name='category-list'),
	url(r'^category/(?P<pk>\d+)/$', CategoryDetailAPIView.as_view(), name='category-detail'),
	url(r'^category/(?P<pk>\d+)/edit/$', CategoryUpdateAPIView.as_view(), name='category-update'),
	url(r'^category/(?P<pk>\d+)/delete/$', CategoryDeleteAPIView.as_view(), name='category-delete'),

# 	item
	url(r'^item/create$', ItemCreateAPIView.as_view(), name='item-create'),
	url(r'^item$', ItemListAPIView.as_view(), name='item-list'),
	url(r'^item/(?P<pk>\d+)/$', ItemDetailAPIView.as_view(), name='item-detail'),
	url(r'^item/(?P<pk>\d+)/edit/$', ItemUpdateAPIView.as_view(), name='item-update'),
	url(r'^item/(?P<pk>\d+)/delete/$', ItemDeleteAPIView.as_view(), name='item-delete'),

# order
	url(r'^order/create$', OrderCreateAPIView.as_view(), name='order-create'),
	url(r'^order$', OrderListAPIView.as_view(), name='order-list'),
	url(r'^order/(?P<pk>\d+)/$', OrderDetailAPIView.as_view(), name='order-detail'),
	url(r'^order/(?P<pk>\d+)/edit/$', OrderUpdateAPIView.as_view(), name='order-update'),
	url(r'^order/(?P<pk>\d+)/delete/$', OrderDeleteAPIView.as_view(), name='order-delete'),

# table
	url(r'^table/create$', TableCreateAPIView.as_view(), name='table-create'),
	url(r'^table$', TableListAPIView.as_view(), name='table-list'),
	url(r'^table/(?P<pk>\d+)/$', TableDetailAPIView.as_view(), name='table-detail'),
	url(r'^table/(?P<pk>\d+)/edit/$', TableUpdateAPIView.as_view(), name='table-update'),
	url(r'^table/(?P<pk>\d+)/delete/$', TableDeleteAPIView.as_view(), name='table-delete'),
]