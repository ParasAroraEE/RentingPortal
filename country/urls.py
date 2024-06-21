from django.urls import path, include
from rest_framework.routers import DefaultRouter
from country import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename="api_countries")
router.register(r'states', views.StateViewSet, basename="api_states")
router.register(r'cities', views.CityViewSet, basename="api_cities")

urlpatterns = [
    path('', include(router.urls)),
]
