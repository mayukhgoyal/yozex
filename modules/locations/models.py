from tabnanny import verbose
from django.db import models

# Create your models here.
class Location(models.Model):
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    location = models.CharField(verbose_name=("Location"), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.location)
