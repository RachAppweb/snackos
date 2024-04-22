from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    
    return render(request,'main/index.html')

def more(request,category_slug=None):
    if category_slug != None:
        category=get_object_or_404(Category,slug=category_slug)
        menu=Menu.objects.filter(category=category,is_availabele=True).order_by('id')
    else:
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