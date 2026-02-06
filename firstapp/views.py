from django.shortcuts import render, redirect

from .forms import ItemForm

from .models import Item

# Create your views here.

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'firstapp/success.html')
    else:
        form = ItemForm()
    return render(request, 'firstapp/create_item.html', {'form': form})     

def items_list(request):
    
    items = Item.objects.all()
    return render(request, 'firstapp/items_list.html', {'items': items})


def home(request):

    return render(request, 'firstapp/home.html')

def love(request):
    return render(request, 'firstapp/love.html')
