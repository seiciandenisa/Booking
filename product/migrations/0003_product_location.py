# Generated by Django 4.2.4 on 2023-09-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
