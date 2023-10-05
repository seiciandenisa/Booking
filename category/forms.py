from django import forms
from django.forms import TextInput

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a category name'}),
        }

    # validare astfel incat categoriile sa fie unice
    def clean(self):
        cleaned_data = self.cleaned_data

        get_name = cleaned_data['name']
        check_names = Category.objects.filter(name=get_name)
        if check_names:
            message = 'This category already exists!'
            self._errors['name'] = self.error_class([message])

        return cleaned_data


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter category name'})
        }
