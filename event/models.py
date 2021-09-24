from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length=200)
    activities = models.CharField(max_length=9000)
    budget = models.IntegerField(default=1)


    def save(self):
        if self._state.adding:
            self.event_id = Event.objects.all().count() + 1
            return super(Event, self).save()
        else:
            eventExists = Event.objects.filter(event_id=self.event_id)
            eventExists.update(budget = self.budget)