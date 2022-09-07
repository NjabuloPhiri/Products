from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Product
from .forms import ProductCreateForm


class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.order_by('-created_on')
    template_name = 'home.html'
    context_object_name = 'object_list'
    paginate_by = 2


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'post_product.html'
    form_class = ProductCreateForm

    def form_valid(self, form):
        form.instance.retailer = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = ProductCreateForm

    def form_valid(self, form):
        form.instance.retailer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product_update = self.get_object()
        if self.request.user == product_update.retailer:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        product_update = self.get_object()
        if self.request.user == product_update.retailer:
            return True
        return False
