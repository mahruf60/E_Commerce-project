from django.shortcuts import render,redirect
from main_app.form import Contactfrom
from main_app.models import *
# Create your views here.
def index(request):
    banner= Banner.objects.all()
    product=Product.objects.all().order_by ('?')
    
    context={
        'banner':banner,
        'product':product,
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == 'POST':
        form = Contactfrom(request.POST)
        print(form,'SSSSSS')
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Contactfrom()
    return render(request,'contact.html',{'form':Contactfrom})


def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    related_products=Product.objects.filter(category=product.category).exclude(id=product.pk)
    
    context = {
        'product':product,
        'related_products':related_products,
    }
    return render(request,'product_detail.html',context)