from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article

# Create your views here.
def home(request):
    return HttpResponse('<html><body><p>Bienvenue !</p></body></html>')

def article_list(request):
    articles = Article.objects.all()
    context = {
        'article_list': articles
    }
    return render(request, "maBoutique/article_list.html", context)

def article_detail(request, id):
    each_article = Article.objects.get(id=id)
    context = {
        'article_detail': each_article
    }
    return render(request, "maBoutique/article_detail.html", context)

def article_delete(request, id):
    each_article = Article.objects.get(id=id)
    each_article.delete()
    return HttpResponseRedirect('/maBoutique/article_list.html')
from django.shortcuts import render, redirect

from .form import ArticleForm

def articleForm(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Assuming you have a URL name 'article_list' for redirecting
    else:
        # If it's not a POST request, it's probably a GET request
        form = ArticleForm()  # Create an empty form
    return render(request, 'maBoutique/form.html', {'form': form})

from datetime import datetime
from django.shortcuts import render

def accueil(request):
    context = {
        'current_date': datetime.now()
    }
    return render(request, "maBoutique/accueil.html", context)
