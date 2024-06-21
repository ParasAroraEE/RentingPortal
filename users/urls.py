from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register(r'userprofile', views.UserProfileViewSet, basename="api_userprofiles")
router.register(r'user', views.UserViewSet, basename="api_user")

urlpatterns = [
    path('', include(router.urls)),
]
