from django.shortcuts import render,redirect
from main_app.form import Contactfrom
from main_app.models import *
# Create your views here.
def index(request):
    banner= Banner.objects.all()
    
    context={
        'banner':banner
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


def product(request):
    return render(request,'product.html')