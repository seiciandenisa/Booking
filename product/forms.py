from django import forms
from django.forms import TextInput, NumberInput, Textarea, Select

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your product title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your product description'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter location'})
        }

    # validare astfel incat sa nu existe un produs cu acelasi titlu
    def clean(self):
        cleaned_data = self.cleaned_data

        get_title = cleaned_data['title']
        check_titles = Product.objects.filter(title=get_title)
        if check_titles:
            message = 'This product already exists!'
            self._errors['title'] = self.error_class([message])

        return cleaned_data


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter product title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter product description'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter location'})
        }
