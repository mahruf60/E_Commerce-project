from django.urls import path 
from user_app.views import *

urlpatterns = [
    path('register/',register,name='register'),
]
