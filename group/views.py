from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from group.models import Group
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def get_group_name(request, group_name):
    if request.method == 'GET':
        try:
            group = Group.objects.filter(name="GROUP A").first()
            expectedGroup = Group.objects.all()[0]
            
            response = json.dumps([{'Group': expectedGroup.name + group.name}])
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_group(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        gName = payload["group_name"]
        group = Group(name=gName)
        try:
            group.save()
            s = Group.objects.get(name=gName)

            response = json.dumps([{'Success': 'Group created successfully' + s}])
        except:
            response = json.dumps([{'Error': group.name}])
        return HttpResponse(response, content_type='text/json')