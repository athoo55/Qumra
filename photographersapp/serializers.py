# photographers/serializers.py
from rest_framework import serializers
from .models import Photographer, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotographerSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Photographer
        fields = '__all__'
