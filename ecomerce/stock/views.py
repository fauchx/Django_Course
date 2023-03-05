from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{"formulario":form})
    else:    
        form = ProductForm()
        return render(request,"index.html",{"formulario":form})