from django.urls import path 
from user_app.views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('logout/', logout_view, name='logout'),
    
    path('profile/',profile,name='profile-page'),
    path('profile/update',profileupdate,name='profileupdate-page'),
]
