# waste_app/models.py
from django.db import models

class WasteItem(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name
