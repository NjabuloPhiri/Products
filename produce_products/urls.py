from django.urls import path
from .views import ProductsListView, ProductsDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('product/new/', ProductCreateView.as_view(), name='post_product'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('', ProductsListView.as_view(), name='home'),
]
