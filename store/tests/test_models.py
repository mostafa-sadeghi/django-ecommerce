from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.data = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        self.assertEqual(isinstance(self.data, Category), True)

    def test_category_model_entry_return(self):
        self.assertEqual(str(self.data), 'django')


class TestProductModel(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name="django", slug="django")
        self.created_by = User.objects.create(username="nikan")
        self.data = Product.objects.create(
            category=category, created_by=self.created_by, title='django', slug='django', price=22.9)

    def test_product_model_creator(self):
        self.assertEqual(self.data.created_by, self.created_by)

    def test_product_model_entry_return(self):
        self.assertEqual(str(self.data), 'django')
