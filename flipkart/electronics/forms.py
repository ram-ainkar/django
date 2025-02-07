# from django import forms
# from .models import Product

# class ProductForm(forms.ModelForm):
#     class meta:
#         model = Product
#         fields = ["name", "desc","price"]
from django import forms
from .models import Product  # Ensure the model is imported

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Link the form to the Product model
        fields = '__all__'  # Or specify the fields explicitly
