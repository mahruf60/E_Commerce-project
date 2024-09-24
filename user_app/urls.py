from django.urls import path 
from user_app.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('logout/', logout_view, name='logout'),
    
    path('profile/',profile,name='profile-page'),
    path('profile/update',profileupdate,name='profileupdate-page'),
    
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='user_app/passwordchange.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='user_app/passwordchange_done.html'),name='password_change_done'),
]
