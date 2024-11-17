from django.urls import path
from main_app.views import *
   
urlpatterns =[

    path('',index,name="index"),

    path('contact/',contact,name="contact"),

    path('product_de/<int:pk>/',product_detail,name="product_detail"),
    
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increment/<int:item_id>/', increment_cart_item, name='increment_cart_item'),
    path('decrement/<int:item_id>/', decrement_cart_item, name='decrement_cart_item'),
    
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/',remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('checkout/',checkout,name='checkout'),
    path('payment/<int:order_id>/',payment,name='payment'),
    path('order_confirmation/<int:order_id>/',order_confirmation,name='order_confirmation'),
    path('order_history/',order_history,name='order_history'),
]