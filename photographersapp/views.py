# photographers/views.py
from rest_framework import viewsets
from .models import Photographer, Photo
from .serializers import PhotographerSerializer, PhotoSerializer

class PhotographerViewSet(viewsets.ModelViewSet):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
