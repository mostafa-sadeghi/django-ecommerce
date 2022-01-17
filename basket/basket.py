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

        self.session.modified = True
        print(product_id, product_qty, self.basket)

    def __len__(self):
        items = [item['qty'] for item in self.basket.values()]
        return sum(items)
