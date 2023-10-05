from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from userextend.forms import UserCreationNewForm


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_userextend.html'
    model = User
    form_class = UserCreationNewForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.save()

        return redirect('login')


# class History(FormView):
#     template_name = 'userextend/history.html'
#     model = User
#     form_class = ''
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         instance = form.save()
#
#         history = History(
#             instance=instance,
#             old_content=instance.content,
#             date_modified=instance.date_modified
#         )
#         history.save()
#
#         return super().form_valid(form)
