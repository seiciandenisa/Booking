from django.db import models

from category.models import Category


# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.title}'
