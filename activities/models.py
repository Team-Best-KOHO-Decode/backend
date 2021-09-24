from django.db import models
from group.models import Group

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=2000)
    address = models.CharField(max_length=500)
   # lat_long = models.CharField()

    def turn_to_json(self):
        res = {
                'name': self.name,
                'cost': self.cost,
                'description': self.description,
                'image': self.image,
                'address': self.address,
                #'lat_long': self.lat_long,
                }
        return res
