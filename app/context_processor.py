from .models import Menu,Events,SnackInfo,Category
from django.shortcuts import redirect
def foods(request):
    menu=Menu.objects.all().filter(is_availabele=True).order_by('id')[:3]
    
    return dict(menu=menu)
def events(request):
    try:
       events=Events.objects.all()
    except(Events.DoesNotExist,TypeError):
          return redirect('index')
    
    return dict(events=events)

def about(request):
    try:
        info=SnackInfo.objects.all().first()
        context={
            "snackinfo":info
        }
    except(SnackInfo.DoesNotExist,TypeError):
        return redirect('index')
    return dict(info=info)
    
def category(request):
    category=Category.objects.all()
    return dict(category=category)