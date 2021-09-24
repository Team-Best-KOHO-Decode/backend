from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from activities.models import Activity
from group.models import Group
import json
from django.views.decorators.csrf import csrf_exempt
from ast import literal_eval

# Create your views here.
def get_events(request):
    if request.method == 'GET':
        try:
            activities = Activity.objects.all().iterator()
            response = []
            for getActivity in activities:
                temp = getActivity.turn_to_json()
                response.append(temp)
            response = json.dumps(response) 
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
    return HttpResponse(response, content_type='text/json')

def get_events_by_budget(request, budget):
    if request.method == 'GET':
        try:
            activities = Activity.objects.filter(cost__lte=budget).iterator()
            response = []
            for getActivity in activities:
                temp = getActivity.turn_to_json()
                response.append(temp)
            response = json.dumps(response) 
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
    return HttpResponse(response, content_type='text/json')
