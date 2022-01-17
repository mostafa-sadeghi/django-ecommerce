from django.shortcuts import render, get_object_or_404
from .basket import Basket
from django.http import JsonResponse
from store.models import Product


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('productid')
        product_qty = request.POST.get('productqty')
        product = get_object_or_404(Product, pk=product_id)
        basket.add(product, product_qty)
        basket_qty = basket.__len__()
    return JsonResponse({'qty': basket_qty})
