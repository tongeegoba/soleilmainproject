from django.urls import path, re_path, include
from .api.views import ArticleListApiView, ArticleCreateApiView
from .views import list

app_name = 'articles'

urlpatterns = [
    re_path(r'^api/list/$',ArticleListApiView.as_view() ,name='articles_api_list'),
    re_path(r'^list/$',list ,name='articles_list'),
    re_path(r'^api/create/$',ArticleCreateApiView.as_view() ,name='articles_api_create'),
]