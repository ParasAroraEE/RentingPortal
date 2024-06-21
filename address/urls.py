from django.urls import path, include
from rest_framework.routers import DefaultRouter
from address import views

router = DefaultRouter()
router.register(r'address', views.AddressViewSet, basename="address")

urlpatterns = [
    path('', include(router.urls)),
]
