from django.shortcuts import render
from django.http import HttpResponse
from event.models import Event
from group.models import Group
import json
from django.views.decorators.csrf import csrf_exempt
from ast import literal_eval
import heapq
from bson import ObjectId
# Create your views here.

@csrf_exempt
def get_event_by_id(request, event_id):
    if request.method == 'GET':
        try:
            getEvent = Event.objects.get(pk=ObjectId(event_id))
            response = json.dumps({'event_id': str(getEvent._id), 'event_name': getEvent.name, 'budget': getEvent.budget, 'activities': getEvent.activities})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        event_name_input = payload["event_name"]
        group_id_input = payload["group_id"]
        if "event_budget" in payload:
            event_budget = payload["event_budget"]
        else:
            event_budget = 1
        createdEvent = Event(name = event_name_input, budget = event_budget, activities = "{}")
        try:
            createdEvent.save()

            group = Group.objects.get(id=group_id_input)
            eventList = literal_eval(group.events)
            eventList.append(createdEvent._id)
            group.events = str(list(dict.fromkeys(eventList)))
            group.save()
            activities = createdEvent.get_sorted_activities()
            response = json.dumps({'event_id': str(createdEvent._id), 'event_name': createdEvent.name, 'budget': createdEvent.budget, 'activities': activities})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def update_event_budget(request):
    if request.method == 'PUT':
        payload = json.loads(request.body)
        event_id = ObjectId(payload["event_id"])
        event_budget = payload["event_budget"]
        updatedEvent = Event.objects.get(pk=event_id)
        updatedEvent.budget = event_budget
        try:
            updatedEvent.save()
            response = json.dumps({'event_id': str(updatedEvent.pk), 'event_name': updatedEvent.name, 'budget': updatedEvent.budget, 'activities': updatedEvent.get_sorted_activities()})
        except Exception as e:

            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def select_activities(request):
    if request.method == 'PUT':
        payload = json.loads(request.body)
        updatedEvent = Event.objects.get(pk=ObjectId(payload['event_id']))
        event_activities = json.loads(updatedEvent.activities)
        activities = payload['activities']
        for activity in activities:
            if str(activity) not in event_activities:
                event_activities[str(activity)] = 1
            else:
                event_activities[str(activity)] += 1
        
        updatedEvent.activities = json.dumps(event_activities)
        updatedEvent.save()

        res = {}
        res['event_id'] = payload['event_id']
        res['event_name'] = updatedEvent.name
        
        heap = updatedEvent.get_sorted_activities()

        res['activities'] = heap

        response = json.dumps(res)

        return HttpResponse(response, content_type='text/json')





