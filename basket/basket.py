class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if basket is None:
            basket = self.session['skey'] = {}
        self.basket = basket
