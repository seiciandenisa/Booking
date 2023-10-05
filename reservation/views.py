from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from reservation.forms import ReservationForm, ReservationUpdateForm
from reservation.models import Reservation


# Create your views here.

class ReservationCreateView(PermissionRequiredMixin, CreateView, SuccessMessageMixin):
    template_name = 'reservation/create_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('list-of-reservations')
    success_message = 'Reservation was made successfully!'
    permission_required = 'reservation.add_reservation'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(name=self.object.name)


class ReservationListView(PermissionRequiredMixin, ListView):
    template_name = 'reservation/list_of_reservations.html'
    model = Reservation
    context_object_name = 'all_reservations'
    permission_required = 'reservation.add_reservation'

    def get_queryset(self):
        return Reservation.objects.all()


class ReservationUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'reservation/update_reservation.html'
    model = Reservation
    form_class = ReservationUpdateForm
    success_url = reverse_lazy('list-of-reservations')
    permission_required = 'reservation.add_reservation'


class ReservationDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'reservation/delete_reservation.html'
    model = Reservation
    success_url = reverse_lazy('list-of-reservations')
    permission_required = 'reservation.add_reservation'


class ReservationDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'reservation/detail_reservation.html'
    model = Reservation
    permission_required = 'reservation.add_reservation'
