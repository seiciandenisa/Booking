from django.db import models

from product.models import Product


# Create your models here.

class Reservation(models.Model):
    date_in = models.DateField()
    date_out = models.DateField()

    def __str__(self):
        return f'{self.date_in}'
