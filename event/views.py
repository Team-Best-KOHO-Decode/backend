from django.shortcuts import render
from django.http import HttpResponse
from event.models import Event
from group.models import Group
import json
from django.views.decorators.csrf import csrf_exempt
from ast import literal_eval
# Create your views here.

@csrf_exempt
def get_event_by_id(request, event_id):
    if request.method == 'GET':
        try:
            event = Event.objects.get(event_id=event_id)
            response = json.dumps({'event_id': event.event_id, 'event_name': event.name, 'budget': event.budget, 'activities': event.activities})
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
        event = Event(name = event_name_input, budget = event_budget, activities = "[]")
        try:
            event.save()

            group = Group.objects.get(id=group_id_input)
            eventList = literal_eval(group.events)
            eventList.append(event.event_id)
            group.events = str(list(dict.fromkeys(eventList)))
            group.save()

            response = json.dumps({'event_id': event.event_id, 'event_name': event.name, 'budget': event.budget, 'activities': event.activities})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def update_event_budget(request):
    if request.method == 'PUT':
        payload = json.loads(request.body)
        event_id = payload["event_id"]
        event_budget = payload["event_budget"]
        event = Event.objects.get(event_id=event_id)
        event.budget = event_budget
        try:
            event.save()
            response = json.dumps({'event_id': event.event_id, 'event_name': event.name, 'budget': event.budget, 'activities': event.activities})
        except Exception as e:

            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')






