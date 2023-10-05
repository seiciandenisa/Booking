import django_filters
from django import forms

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    list_category = [(product.category.id, product.category.name.upper()) for product in
                     Product.objects.filter(is_active=True)]
    list_locations = [(product.location, product.location) for product in Product.objects.filter(is_active=True)]

    category = django_filters.ChoiceFilter(choices=list(set(list_category)),
                                           widget=forms.Select(attrs={'class': 'form-select'}))

    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Minimum price',
                                            widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Please choose a minimum price',
                                                                            'type': 'number'}))
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Maximum price',
                                            widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Please choose a maximum price',
                                                                            'type': 'number'}))
    location = django_filters.ChoiceFilter(choices=list(set(list_locations)),
                                           widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Product
        fields = ['category', 'price_gte', 'price_lte', 'location']
