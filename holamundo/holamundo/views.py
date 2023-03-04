from django.http import HttpResponse

def saludo(request):
    return HttpResponse("HABLAME MANO")

def adulto(request,edad):
   if edad >= 18:
    return HttpResponse("Es mayor de edad") 
   else:
    return HttpResponse("No eres mayor de edad") 