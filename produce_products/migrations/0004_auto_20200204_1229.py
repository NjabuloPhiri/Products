# Generated by Django 3.0.3 on 2020-02-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce_products', '0003_auto_20200204_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]