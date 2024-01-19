from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
	path('home/', home, name = 'home'), 
	path('resume/', gen_resume, name = 'resume'),
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
]