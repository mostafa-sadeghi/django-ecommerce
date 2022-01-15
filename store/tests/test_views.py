from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from store.models import Product, Category


class TestViewResponses(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(username='nikan')
        self.category = Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(
            category=self.category, created_by=self.user, image='چند_هدفه.png', title='django', slug='django', price=22.9)

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.client.get(
            reverse('store:category_detail', args=['django']))
        self.assertEqual(response.status_code, 200)
