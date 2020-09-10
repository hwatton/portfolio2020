from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagetwo/', views.pagetwo, name='pagetwo'),
    path('about/', views.about, name='about'),
    path('graphics/', views.graphics, name='graphics'),
    ]
