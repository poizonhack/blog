from django.shortcuts import render
from .models import Article
# Create your views here.

def accueil(request):
    list_articles=Article.objects.all()
    context={"liste_articles":list_articles}
    return render(request,"index.html",context)


