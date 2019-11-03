from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Product#, Person
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

'''
class CustomUserCreationForm(UserCreationForm, forms.ModelForm):
    
    class Meta:
        model=CustomUser
        fields=('username',
                'first_name', 
                'last_name', 
                'address', 
                'country', 
                'email')
        #country=CountryField(blank_label='(Select Country)').formfield()
        widgets = {'country': CountrySelectWidget()}
 '''      
 
class CustomUserCreationForm(UserCreationForm, forms.ModelForm):
    
    class Meta:
        model=CustomUser
        fields=('username',
                'first_name', 
                'last_name', 
                'address', 
                'country', 
                'email')
        #country=CountryField(blank_label='(Select Country)').formfield()
        widgets = {'country': CountrySelectWidget()}
        
    def save(self, commit=True):
        user=super(CustomUserCreationForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user 

class CustomUserChangeForm(UserChangeForm, forms.ModelForm):
    
    class Meta:
        model=CustomUser
        fields=('username',
                'first_name', 
                'last_name', 
                'address', 
                'country', 
                'email', 
                'password')
        #country=CountryField().formfield()
        widgets = {'country': CountrySelectWidget()}
 
        
class ProductCreationForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields=('price', 
                'title', 
                'descr', 
                'product_image', 
                'country', 
                'category')
        widgets = {'country': CountrySelectWidget()}
        
        