from django.conf.urls import url
from django.contrib import admin

from .views import(
	StaffCreateAPIView,
	StaffListAPIView,
	StaffDetailAPIView,
	StaffUpdateAPIView,
	StaffDeleteAPIView
	)

urlpatterns = [
	url(r'^create$', StaffCreateAPIView.as_view(), name='create'),
	url(r'^$', StaffListAPIView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', StaffDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', StaffUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', StaffDeleteAPIView.as_view(), name='delete'),
]