from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('signup/',views.sign_up,name='signuppage'),
    path('login/',views.user_login,name='loginpage'),
    path('profile/',views.user_profile,name='profilepage'),
    path('logout/',views.user_logout,name='logoutpage'),
 ]