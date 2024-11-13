from django.shortcuts import render
from .models import *

# Create your views here.
def main_page(request):
    return render(request, 'one_task/menu.html')

def shop_page(request):
    game = Game.objects.all()
    context = {
        'game': game,
    }
    return render(request, 'one_task/shop_page.html', context)

def cart_page(request):
    return render(request, 'one_task/cart_page.html')

