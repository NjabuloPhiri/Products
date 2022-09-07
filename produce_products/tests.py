from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Product


class ProduceProductsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='Django2020'
        )

        self.product = Product.objects.create(
            product_name='Adidas',
            product_color='Green',
            price='5420',
            retailer=self.user,
        )

    def test_product_instance_exists_in_db(self):
        self.assertTrue(self.product, object)

    # def test_product_update_view(self):
    #     response = self.client.post(reverse('products_update', args='1'), {
    #         'product_name': 'Recently updated product',
    #         'product_color': 'Blue',
    #     })
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_product_delete_view(self):
    #     response = self.client.get(
    #         reverse('products_delete', args='1'))
    #     self.assertEqual(response.status_code, 302)
    #
    # def test_post_product(self):
    #     self.assertEqual(f'{self.product.product_color}', 'Green')
    #     self.assertEqual(f'{self.product.retailer}', 'testuser')
    #
    # def test_user_details(self):
    #     self.assertEqual(f'{self.user}', 'testuser')
    #     self.assertEqual(f'{self.user.email}', 'test@email.com')
