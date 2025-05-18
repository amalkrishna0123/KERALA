from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('about/', views.About, name='about'), 
    path('projects/', views.Projects, name='projects'),  
    path('services/', views.Services, name='services'),
    path('packages/', views.Packages, name='packages'),
    path('blog/', views.Blog, name='blog'),
    path('contact/', views.Contact, name='contact'),
]
