from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
# Create your views here.
def index(request):
    employee = EmployeeForm()
    return render(request,"index.html",{"empleado":employee})