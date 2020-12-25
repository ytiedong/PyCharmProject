from django.urls import path, include
from eigyosystem.eigyo.login import views

urlpatterns = [
    path('', views.logineigyo, name='logineigyo'),  # index
]