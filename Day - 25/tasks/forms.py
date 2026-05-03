from django import forms
from tasks.models import *

class UpdateProfileForm(forms.ModelForm):
    

    class Meta:
        

        model = ProfileModel
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'})
        }

class ProductForm(forms.ModelForm):
    class Meta:

        model = ProductModel
        fields = '__all__'
        exclude = ['total_amount','created_by']