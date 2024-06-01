from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_universities, name='recommend_universities'),
]
