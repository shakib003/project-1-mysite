from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request): # landing page of food app
    # This function handles the request to the landing page of the food app
    return HttpResponse("Hello World!")

# food/item/ will be handled by this function
def item(request): 
    return HttpResponse("This is an item view")
