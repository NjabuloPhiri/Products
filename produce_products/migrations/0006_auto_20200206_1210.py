# Generated by Django 3.0.3 on 2020-02-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce_products', '0005_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
