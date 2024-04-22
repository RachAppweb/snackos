from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('category/<slug:category_slug>/',views.more,name='category'),
    path('more/',views.more,name='more'),
    path('about/',views.about,name='about'),
    path('details/<slug:category_slug>/<slug:food_slug>/',views.food_details,name='food_details'),
]
