from django import forms
from django.forms import Select, TextInput, DateInput

from reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'date_in': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_out': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ReservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'reserved_by': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'date_in': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_out': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
