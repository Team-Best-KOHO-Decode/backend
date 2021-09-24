from django.db import models
import uuid

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    join_code = models.CharField(max_length=5, blank=True, unique=True, default=uuid.uuid4().hex[:5].upper()) 
    # # TODO add refrence to events
    # events = models.ForeignKey(Event)
    # # TODO add refrence to users
    # users = [""]
    