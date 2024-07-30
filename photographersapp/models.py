# photographers/models.py
from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    session_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    photographer = models.ForeignKey(Photographer, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()

    def __str__(self):
        return f"Photo by {self.photographer.name}"
