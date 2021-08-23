from rest_framework import routers
from django.urls import path, include
from . import viewsets

router = routers.DefaultRouter()

router.register(r'company', viewsets.CompanyViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
