from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    
    return render(request,'main/index.html')

def more(request):
    menu=Menu.objects.all().filter(is_availabele=True).order_by('id')
    context={
        'menus':menu
    }
    return render(request,'main/more.html',context)
def about(request):
    
    return render (request,'main/about.html')
def food_details(request,category_slug,food_slug):
    try:
        menu=Menu.objects.get(category__slug=category_slug,slug=food_slug)
        context={
            'menu':menu
        }
    except(Menu.DoesNotExist,TypeError):
        return redirect('index')

    return render(request,'main/food_details.html',context)