from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.forms import CategoryForm, CategoryUpdateForm
from category.models import Category


# Create your views here.

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('home-page')
    permission_required = 'category.add_category'
    success_message = 'Category {name} has been created successfully!'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(name=self.object.name)


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'
    permission_required = 'category.view_list_of_categories'

    def get_queryset(self):
        return Category.objects.all()


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list-of-categories')
    permission_required = 'category.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list-of-categories')
    permission_required = 'category.delete_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'category/detail_category.html'
    model = Category
    permission_required = 'category.view_category'
