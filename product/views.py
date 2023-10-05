from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from product.filters import ProductFilter
from product.forms import ProductForm, ProductUpdateForm
from product.models import Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home-page')
    success_message = 'Product {title} was successfully created!'
    permission_required = 'product.add_product'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(title=self.object.title)


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'
    permission_required = 'product.view_list_of_products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.filter(is_active=True)  # stochez produsele care vin in interfata, cele active
        filters = ProductFilter(self.request.GET,
                                queryset=products)  # raman doar produsele care indeplinesc cerintele filtrarii
        products = filters.qs  # reinitializez variabila, dintre toate produsele active, raman doar cele care vin in urma filtrarii
        context['all_products'] = products  # trimit in interfata produsele
        context['form_filter'] = filters.form  # trimit in interfata formularul de filtrare

        return context


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('list-of-products')
    permission_required = 'product.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list-of-products')
    permission_required = 'product.delete_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'product/detail_product.html'
    model = Product
    permission_required = 'product.view_product'


def get_all_products_per_category(request, pk):  # pk este id-ul categoriei
    products_per_category = Product.objects.filter(category_id=pk)
    return render(request, 'product/product_per_category.html', {'products_category': products_per_category})
