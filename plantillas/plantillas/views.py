from django.shortcuts import render;

def simple(request):
    return render(request,"simple.html",{})

def dinamico(request,nombre):
    categories = ['code','design','marketing']
    context = {"nombre" : nombre, 'categories' : categories}
    return render(request,"contexto.html", context)
