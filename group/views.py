from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group

import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def get_group_by_id(request, group_id):
    if request.method == 'GET':
        try:
            group = Group.objects.get(id=group_id)
            response = json.dumps({'group_id': group.id, 'group_name': group.name, 'group_join_code': group.join_code, 'group_events': stringToList(group.events)})
        except Exception as e:
            response = json.dumps({'Error': str(e)})
        return HttpResponse(response, content_type='text/json')

@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        group_name_input = payload["group_name"]
        group = Group(name = group_name_input, events = "[]")
        try:
            group.save()
            print()
            response = json.dumps({'group_id': group.id, 'group_name': group.name, 'group_join_code': group.join_code, 'group_events': stringToList(group.events)})
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
        return HttpResponse(response, content_type='text/json')

def stringToList(listString):
    return listString[1:-1].split(',')
