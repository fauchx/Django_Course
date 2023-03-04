from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry
# Create your views here.
def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all()

    #obtener los datos filtrando por condicion

    #filtrado = Author.objects.filter(email="andrea61@example.org")

    #ordenar los elementos
    orders = Author.objects.all().order_by("email")

    #Obtencion de elementos cuyo id<15
    filtrado = Author.objects.all().filter(id__lte=15)

    #contiene
    contiene = Author.objects.all().filter(name__contains="yes")

    return render(request,"post/queries.html",{"authors": authors,"filtrado":filtrado,"ordenado":orders,"contiene":contiene})

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Fabian Urrutia"
    author.email ="fabian28@gmail.com"
    author.save()

    return HttpResponse("Modificado")