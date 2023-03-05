from django.http import HttpResponse
from django.shortcuts import render
from .forms import ComentForm, ContactForm

def forms(request):
    comment = ComentForm({"name":"Kebin Durant","url":"http://nba.com","comment":"curry es mejor"})
    return render(request,"forms.html",{"formulario":comment})

def goal(request):
    if request.method != "POST":
        return HttpResponse("MANO NO")
    else:
        return HttpResponse(request.POST["name"])
    
def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request,"widget.html",{"formulario":form})
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #ACA si es valido
            return HttpResponse("R mano")
        else:
            #ACA si no es valido
            return render(request,"widget.html",{"formulario":form})