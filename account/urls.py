from django.urls import path
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    #path('login/', views.user_login, name="user_login")
    path('login/', auth_views.login, name='user_login'),
    path('logout/', auth_views.logout, {'template_name': "account/logout.html"}, name='user_logout'),
    path('register/', views.register, name="user_register"),
    path('password-change/', auth_views.password_change,
         {"post_change_redirect": "/account/password-change-done/"}, name="password_change"),
    path("password-change-done/", auth_views.password_change_done, name="password_change_done"),
]
