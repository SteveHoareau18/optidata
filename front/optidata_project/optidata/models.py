# optidata/models.py
from django.db import models

class Widget(models.Model):
    name = models.CharField(max_length=100)
    view_path = models.CharField(max_length=255, blank=True)  # chemin de la vue, optionnel ici
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=0)
    width = models.FloatField(default=1)
    height = models.FloatField(default=1)

    def __str__(self):
        return self.name
