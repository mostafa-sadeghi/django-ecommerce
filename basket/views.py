from django.shortcuts import render
from .basket import Basket
from django.http import JsonResponse


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
    return JsonResponse({'number': 'number'})
