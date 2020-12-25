from django.urls import path
from eigyosystem.eigyo.menu import views

urlpatterns = [
    # 売上
    path('', views.index, name='index'),  # index
]