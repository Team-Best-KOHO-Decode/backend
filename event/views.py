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
            event = Event.objects.get(pk=ObjectId(event_id))
            response = json.dumps({'event_id': str(event._id), 'event_name': event.name, 'budget': event.budget, 'activities': event.activities})
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
        event = Event(name = event_name_input, budget = event_budget, activities = "{}")
        try:
            event.save()

            group = Group.objects.get(id=group_id_input)
            eventList = literal_eval(group.events)
            eventList.append(event._id)
            group.events = str(list(dict.fromkeys(eventList)))
            group.save()
            activities = event.get_sorted_activities()
            response = json.dumps({'event_id': str(event._id), 'event_name': event.name, 'budget': event.budget, 'activities': activities})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def update_event_budget(request):
    if request.method == 'PUT':
        payload = json.loads(request.body)
        event_id = ObjectId(payload["event_id"])
        event_budget = payload["event_budget"]
        event = Event.objects.get(pk=event_id)
        event.budget = event_budget
        try:
            event.save()
            response = json.dumps({'event_id': str(event.pk), 'event_name': event.name, 'budget': event.budget, 'activities': event.get_sorted_activities()})
        except Exception as e:

            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def select_activities(request):
    if request.method == 'PUT':
        payload = json.loads(request.body)
        event = Event.objects.get(pk=ObjectId(payload['event_id']))
        print(event.activities)
        event_activities = json.loads(event.activities)
        activities = payload['activities']
        for activity in activities:
            if str(activity) not in event_activities:
                event_activities[str(activity)] = 1
            else:
                event_activities[str(activity)] += 1
            print(str(activity), event_activities)
        
        event.activities = json.dumps(event_activities)
        event.save()

        res = {}
        res['event_id'] = payload['event_id']
        res['event_name'] = event.name
        
        heap = event.get_sorted_activities()

        res['activities'] = heap

        response = json.dumps(res)

        return HttpResponse(response, content_type='text/json')





