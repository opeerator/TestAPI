from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request, JsonResponse
from .models import Name
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def hello(request):
    try:
        client_name = request.GET['name']
        # name_instance = Name()
        # name_instance.name = client_name
        # name_instance.save()
        mylist = {
            'meta' : {'status' : 200},
            'data' : {'message': 'hello, ' + client_name}
        }
        return JsonResponse(mylist)
    except:
        return HttpResponse("There is a problem with that input!")
