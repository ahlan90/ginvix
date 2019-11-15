from django.urls import include, path
from rest_framework import routers

from festas import views

router = routers.DefaultRouter()
router.register(r'festas', views.FestaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]