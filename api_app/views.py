from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpRequest, request
from .models import Name
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def hello(request):
    try:
        client_name = request.GET['name']
        name_instance = Name()
        name_instance.name = client_name
        return HttpResponse(name_instance.name)
        name_instance.save()
    except:
        return HttpResponse("There is a problem with that input!")
