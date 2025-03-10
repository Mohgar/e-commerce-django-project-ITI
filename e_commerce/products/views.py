from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView, RedirectView
from .models import Category, Product , Cart, CartItem
from .forms import ProductForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    
   


class CategoryListView(ListView):
    model = Category
    template_name = 'cateogry.html'
    context_object_name = 'cateogrys'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    


class CategoryProductListView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'
   

    def get_queryset(self):
       
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        return Product.objects.filter(category=category)
    

class ProductSearchListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    # Handle the search functionality
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Product.objects.filter(title__icontains=query) 
        return Product.objects.all()
    

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('products')  



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('products')  

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products') 

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('products')

    # -------------Cart Views--------------------------#

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart_detail.html'
    context_object_name = 'cart'

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class AddToCartView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('cart_detail')

    def get_redirect_url(self, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return super().get_redirect_url(*args, **kwargs)
    

class RemoveFromCartView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('cart_detail')

    def get_redirect_url(self, *args, **kwargs):
        cart_item_id = self.kwargs.get('cart_item_id')
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return super().get_redirect_url(*args, **kwargs)




   

   
   

