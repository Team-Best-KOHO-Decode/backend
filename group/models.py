from django.db import models
import uuid

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    join_code = uuid.uuid4().hex[:6].upper()
    events = [""]
    