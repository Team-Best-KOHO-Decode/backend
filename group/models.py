from django.db import models
import uuid

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    join_code = models.CharField(max_length=5, blank=True, unique=True, default=uuid.uuid4().hex[:5].upper()) 
    # JSON string of events and activities with ratings
    events = models.CharField(max_length=9000)
    