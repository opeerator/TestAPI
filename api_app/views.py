from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request, JsonResponse
from .models import Name
from django.views.decorators.csrf import csrf_exempt

def memoize(f):
    fibs = {}
    def helper(x):
        if x not in fibs:
            fibs[x] = f(x)
        return fibs[x]
    return helper

@memoize
def F(n): 
    a = 0
    b = 1
    place = 0
    if n == 0:
        return a
    while b != n:
        c = a + b 
        a = b 
        b = c
        place += 1
        
    return place + 1

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


@csrf_exempt
def fibonacci(request):
    try:
        number = request.GET['index']
        finalfib = F(int(number))
        mylist = {
            'meta' : {'status' : 200},
            'data' : {'fibNumber': finalfib}
        }
        return JsonResponse(mylist)
    except:
        return HttpResponse("There was a problem with calculating fibonnaci!")

