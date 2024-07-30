# photographers/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotographerViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'photographers', PhotographerViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
