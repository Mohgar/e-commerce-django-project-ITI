from django.urls import path
from .views import (
    ProductListView, CategoryListView, ProductDetailView,
    CategoryProductListView, ProductSearchListView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, CategoryCreateView,
    CartDetailView, AddToCartView, RemoveFromCartView,
)
 
urlpatterns = [
    path('', ProductListView.as_view(), name='products'), 
    path('cateogry/', CategoryListView.as_view(), name='cateogry'),  
    path('home/<int:pk>/', ProductDetailView.as_view(), name='single'),  
    path('category/<int:category_id>/products/', CategoryProductListView.as_view(), name='category_products'),  
    path('products/', ProductSearchListView.as_view(), name='products_list'),  
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
      
   
]