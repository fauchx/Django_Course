from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(request):
    place = Place(name="El Rolo",address="Cra 1 #56-201")
    place.save()

    resta = Restaurant(place=place,number_of_employees=13)
    resta.save()

    return HttpResponse(resta.place.name)
