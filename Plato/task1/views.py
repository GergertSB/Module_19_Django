from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

# Create your views here.
def main_page(request):
    return render(request, 'one_task/menu.html')

def shop_page(request):
    game = Game.objects.all().order_by()
    per_page = int(request.GET.get('per_page', 1))
    paginator = Paginator(game, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    img_list = ['image/1.png', 'image/2.png', '3.png', '4.png', '5.png']
    context = {
        'game': game,
        'paginator': paginator,
        'page_obj': page_obj,
        'img_list': img_list
    }
    return render(request, 'one_task/shop_page.html', context)

def cart_page(request):
    return render(request, 'one_task/cart_page.html')
