from django.shortcuts import render
from products.models import Product

def index(request):

    context = {'products' : Product.objects.all()[:8]}
    return render(request , 'home/index.html' , context)


def aboutus(request):
    context = {'aboutus' : Product.objects.all()}
    return render(request , 'home/aboutus.html' , context)

def contactus(request):
    return render(request , 'home/contactus.html')