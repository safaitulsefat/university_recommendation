from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('recommend_universities/', views.recommend_universities, name='recommend_universities'),
]
