from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Publication
# Create your views here.
def create(request):
    
    pub1 = Publication.objects.get(id=1)
    resultado = pub1.article_set.all()

    return HttpResponse(resultado)

