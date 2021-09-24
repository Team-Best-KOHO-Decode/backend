from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def create_group(request, group_name):
    a = { 'group-id': 0 }
    return Response(a, status=status.HTTP_201_CREATED)
