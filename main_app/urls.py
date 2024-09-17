from django.urls import path
from main_app.views import *
   
urlpatterns =[

    path('',index,name="index"),

    path('contact/',contact,name="contact"),

    path('product/',product,name="product"),
]