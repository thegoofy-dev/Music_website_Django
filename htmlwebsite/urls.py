from django.contrib import admin
from django.urls import include, path
from htmlwebsite import views

app_name = 'htmlwebsite'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('explore/', views.explore, name = 'explore'),
    path('songpost/<int:id>/', views.song_post, name='song_post'),
    path('search/', views.search, name='search'),
    ]