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
	CategoryQueryAPIView,

	# section
   	SectionCreateAPIView,
   	SectionListAPIView,
   	SectionDetailAPIView,
   	SectionUpdateAPIView,
   	SectionDeleteAPIView,

	#table
    TableCreateAPIView,
   	TableListAPIView,
   	TableDetailAPIView,
   	TableUpdateAPIView,
   	TableDeleteAPIView,
   	RegisteredTableAPIView,
   	UnRegisteredTableAPIView,
   	CheckoutTableAPIView,
   	UnCheckoutTableAPIView,
   	SectionQueryAPIView,
   	TableIdQueryAPIView,
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
	url(r'^item/category/(?P<category>\d+)/$', CategoryQueryAPIView.as_view(), name='categoryItem-query'),


# 	section
   	url(r'^section/create$', SectionCreateAPIView.as_view(), name='section-create'),
   	url(r'^section$', SectionListAPIView.as_view(), name='section-list'),
   	url(r'^section/(?P<pk>\d+)/$', SectionDetailAPIView.as_view(), name='section-detail'),
   	url(r'^section/(?P<pk>\d+)/edit/$', SectionUpdateAPIView.as_view(), name='section-update'),
   	url(r'^section/(?P<pk>\d+)/delete/$', SectionDeleteAPIView.as_view(), name='section-delete'),


# table
	url(r'^table/create$', TableCreateAPIView.as_view(), name='table-create'),
	url(r'^table$', TableListAPIView.as_view(), name='table-list'),
	url(r'^table/(?P<pk>\d+)/$', TableDetailAPIView.as_view(), name='table-detail'),
	url(r'^table/(?P<pk>\d+)/edit/$', TableUpdateAPIView.as_view(), name='table-update'),
	url(r'^table/(?P<pk>\d+)/delete/$', TableDeleteAPIView.as_view(), name='table-delete'),
	#url(r'^table/(?P<slug>[-\w]+)-(?P<value>\d+)/$', TableQueryAPIView.as_view(), name='table-query')
	url(r'^table/registered$', RegisteredTableAPIView.as_view(), name='registered-table-query'),
	url(r'^table/unregistered$', UnRegisteredTableAPIView.as_view(), name='unregistered-table-query'),
	url(r'^table/checkout$', CheckoutTableAPIView.as_view(), name='checkout-table-query'),
	url(r'^table/uncheckout$', UnCheckoutTableAPIView.as_view(), name='uncheckout-table-query'),
	url(r'^table/section/(?P<section>\d+)/$', SectionQueryAPIView.as_view(), name='sectiontable-query'),
	url(r'^table/(?P<slug>[-\w]+)/$', TableIdQueryAPIView.as_view(), name='tableId-query')
]