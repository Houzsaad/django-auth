from django.urls import path
from . views import home,create_item, items_list, love

urlpatterns = [
    path('', home, name='home'),
    
    path('love/', love, name='love'),
    
    path('items/', items_list, name='items_list'),

    path('create_item/', create_item, name='create_item'),

]