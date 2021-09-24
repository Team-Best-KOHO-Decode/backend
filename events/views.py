from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from events.models import Event
from group.models import Group
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_events(request, group_id):
    if request.method == 'GET':
        try:
            events = Event.objects.filter(group_id=group_id).iterator()
            response = []
            for event in events:
                temp = event.turn_to_json()
                response.append(temp)
            response = json.dumps(response) 
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
    return HttpResponse(response, content_type='text/json')
