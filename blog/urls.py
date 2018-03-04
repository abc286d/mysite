from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^$', views.blog_title, name='blog_title'),
    path('<int:article_id>/', views.blog_article, name="blog_detail")
]
