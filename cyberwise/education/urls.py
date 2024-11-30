from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('module/<int:id>/', views.detail, name='detail'),
]

