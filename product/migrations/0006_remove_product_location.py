# Generated by Django 4.2.4 on 2023-09-17 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
    ]
