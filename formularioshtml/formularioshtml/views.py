from django.http import HttpResponse
from django.shortcuts import render

def getform(request):
    return render(request,"form.html",{})

def getgoal(request):
    if request.method != "GET":
        return HttpResponse("MANO NO SEAS BRUTO")

    name = request.GET["nombre"]
    return render(request,"sucess.html", {"nombre":name}) 

def postform(request):
    return render(request,"postform.html",{})

def postgoal(request):
    if request.method != "POST":
        return HttpResponse("MANO NO SEAS BRUTO X2")
    
    info = request.POST["info"]
    return render(request,"postsucess.html",{"info":info})