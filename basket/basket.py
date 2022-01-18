from store.models import Product
from decimal import Decimal


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if basket is None:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        product_id = product.id
        if not str(product_id) in self.basket:
            self.basket[str(product_id)] = {'price': str(
                product.price), 'qty': int(product_qty)}

        self.save()

    def delete(self, id):
        print(id)
        if id in self.basket:
            del self.basket[id]
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['products'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['qty']
            yield item

    def __len__(self):
        items = [item['qty'] for item in self.basket.values()]
        return sum(items)

    def get_total_price(self):
        total = [Decimal(item['price']) * Decimal(item['qty'])
                 for item in self.basket.values()]
        return sum(total)
