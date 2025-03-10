from rest_framework import serializers
from .models import Cart, CartItem

"""
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart #{self.id} for {self.user.username}"
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

   

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items_in_cart_api')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.product.price * self.quantity
    
"""

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']

        def create(self, validate_data):
            user = validate_data.get("user")
            existing_cart = Cart.objects.get(user=user)
            if existing_cart:
                raise serializers.ValidationError("user already have a cart")
            return Cart.objects.create(**validated_data)


         
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ['cart']

        def create(self, validate_data):
            user = self.context['request'].user
            cart=user.api_carts.first()

            if not cart:
                raise serializers.ValidationError("User does not have an existing cart.")
            
            validated_data['cart_id'] = cart.id
            return super().create(validate_data)
        

        
    