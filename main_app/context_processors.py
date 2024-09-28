from main_app.models import *

def g_category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return context

def g_cart(request):
    cart=Cart.objects.count()
    context={
        'cart':cart       
    }
    return context

def g_wishlist(request):
    wishlist=Wishlist.objects.count()
    context={
        'wishlist':wishlist
    }
    return context
