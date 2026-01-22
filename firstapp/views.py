from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item


def home(request):
    return render(request, 'home.html')

def love(request):
    return render(request, 'love.html')

def life(request):
    return render(request, 'life.html')

def items_list(request):
    items = [
        {'name': 'Item 1', 'description': 'Description of Item 1'},
        {'name': 'Item 2', 'description': 'Description of Item 2'},
        {'name': 'Item 3', 'description': 'Description of Item 3'},
    ]
    return render(request, 'items.html', {'items': items})
    