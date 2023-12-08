from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_photo', 'address_line1', 'city', 'state', 'pincode']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control", 'aria-label': "firstname", 'aria-describedby': "addon-wrapping",}),
             'last_name': forms.TextInput(attrs={'class': "form-control", 'aria-label': "lastname", 'aria-describedby': "addon-wrapping",}),
             'username': forms.TextInput(attrs={'class': "form-control", 'aria-label': "username", 'aria-describedby': "addon-wrapping",}),
             'email': forms.EmailInput(attrs={'class': "form-control", 'aria-label': "email", 'aria-describedby': "addon-wrapping",}),
             'password1': forms.PasswordInput(attrs={'class': "form-control", 'aria-label': "password", 'aria-describedby': "addon-wrapping",}),
             'password2': forms.PasswordInput(attrs={'class': "form-control",'aria-label': "cpassword", 'aria-describedby': "addon-wrapping",}),
             'profile_photo': forms.FileInput(attrs={'class': "form-control", 'id': "formFile"}),
             'address_line1': forms.TextInput(attrs={'class': "form-control", 'id':"inputAddress"}),
             'city': forms.TextInput(attrs={'class': "form-control", 'id':"inputCity"}),
             'state': forms.TextInput(attrs={'class': "form-control", 'id':"inputAddress"}),
             'pincode': forms.TextInput(attrs={'class': "form-control", 'id':"inputZip"}),
             
        }