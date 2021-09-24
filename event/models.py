from djongo import models
import json
import heapq

# Create your models here.
class Event(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    activities = models.CharField(max_length=9000)
    # Activities is a dictionary { 'activity_id': vote_count }
    budget = models.IntegerField(default=1)

    '''
    def save(self):
        if self._state.adding:
            self.event_id = Event.objects.all().count() + 1
            return super(Event, self).save()
        else:
            eventExists = Event.objects.filter(event_id=self.event_id)
            eventExists.update(budget = self.budget)
    '''

    def get_sorted_activities(self):
        '''
        Returns a sorted list (vote_number, activity_id)
        '''
        heap = []
        activities_dict = json.loads(self.activities)
        for activity in activities_dict:
            heapq.heappush(heap, (activities_dict[activity], activity))

        return heap
