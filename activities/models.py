from django.db import models
from group.models import Group

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()

    def turn_to_json(self):
        res = {
                'name': self.name,
                'cost': self.cost,
                'description': self.description,
                'rating': self.rating,
                }
        return res

