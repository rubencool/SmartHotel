"""SmartHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from food import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/food/',include("food.api.urls", namespace = 'food-api')),
    url(r'^api/staff/',include("staff.api.urls", namespace = 'staff-api')),
    url(r'^api/customer/',include("customer.api.urls", namespace = 'customer-api')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
