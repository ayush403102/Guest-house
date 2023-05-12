from . import views
from django.urls import path 

urlpatterns = [
    path('index_base/',views.index_base,name="index_base"),
    path('index_office/',views.index_office,name="index_office"),
    path('',views.index_about,name="index_about"),
    path('index_rules/',views.index_rules,name="index_rules"),
    path('index_gallery/',views.index_gallery,name="index_gallery"),
    path('booking/', views.booking, name='booking'),
    path('rooms/', views.rooms, name='rooms'),
]
