from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home-AssociatedServices'),
    path('<str:gcname>/', views.GCDetails, name='GC-AssociatedServices'),
]
