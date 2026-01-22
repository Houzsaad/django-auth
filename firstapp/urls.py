from django.urls import path
from .views import home, items_list, love, life

urlpatterns = [
    path('', home, name='home'),
    path('items/<int:id/', items_list, name= 'items_list'),

    path('love/', love, name='love'),
    
    path('life/', life, name='life'),
]