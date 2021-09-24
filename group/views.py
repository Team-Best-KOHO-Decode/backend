from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group
import uuid

import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def get_group_by_id(request, group_id):
    if request.method == 'GET':
        try:
            getGroup = Group.objects.get(id=group_id)
            response = json.dumps({'group_id': getGroup.id, 'group_name': getGroup.name, 'group_join_code': getGroup.join_code, 'group_events': stringToList(getGroup.events)})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        group_name_input = payload["group_name"]
        joinCode = uuid.uuid4().hex[:5].upper()
        createdGroup = Group(name = group_name_input, events = "[]", join_code = joinCode)
        try:
            createdGroup.save()
            response = json.dumps({'group_id': createdGroup.id, 'group_name': createdGroup.name, 'group_join_code': createdGroup.join_code, 'group_events': stringToList(createdGroup.events)})
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
        return HttpResponse(response, content_type='text/json')

def stringToList(listString):
    return listString[1:-1].split(',')
