from django.db import models
from group.models import Group

# Create your models here.
class Event(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.TextField()

