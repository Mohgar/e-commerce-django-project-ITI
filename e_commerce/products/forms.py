from django import forms
from .models import Product, Category
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'thumbnail', 'rating']

    def clean_thumbnail(self):
        thumbnail_url = self.cleaned_data.get('thumbnail')
        if thumbnail_url: 
            validator = URLValidator()
            try:
                validator(thumbnail_url)
            except ValidationError:
                raise ValidationError("Enter a valid URL.")
            

        return thumbnail_url
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        