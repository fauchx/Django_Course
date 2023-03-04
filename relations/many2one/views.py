from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date


# Create your views here.
def create(request):
    rep = Reporter(name="DeMar",last_name="DeRozan",email="DeMarDeLess@gmail.com")
    art = Article(headline="Vos sos un hpta",pub_date=date(2023,2,26),reporter=rep)
    art1 = Article(headline="Many men", pub_date=date(2002,3,4), reporter=rep)
    art2 = Article(headline="LORD PRETTY FLACKO IN COLOMBIA",pub_date=date(2015,5,28),reporter=rep)
    rep.save()
    art.save()
    art1.save()
    art2.save()

    #resultado = art.reporter.name
    resultado = rep.article_set.all()
    #rep.article_set.count()    
    return HttpResponse(resultado)