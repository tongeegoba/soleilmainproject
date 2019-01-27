from django.shortcuts import render
from .forms import ArticleForm
# Create your views here.


def list(request):
    form = ArticleForm
    return render(request, 'articles.html', {'form':form})