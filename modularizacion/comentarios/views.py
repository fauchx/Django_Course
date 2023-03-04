from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("hola menor")

def create(request):
   # comment = Comment(name="Fabian",score=23,comment="ESTE COMENTARIO")
   # comment.save()
    comment = Comment.objects.create(name="Fabi OU")
    return HttpResponse("crear")

def delete(request):
   # coment = Comment.objects.get(id=1)
   # coment.delete()
   Comment.objects.filter(id=2).delete()
   return HttpResponse("Borrar comentario")

