from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    retailer = models.ForeignKey(User, on_delete=models.CASCADE,)
    product_description = models.TextField()
    product_color = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_image', default='image')

    def __str__(self):
        return '{} {}'.format(self.product_name, self.retailer)

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.pk})
