from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):

    class Meta: 
        model = User
        fields = ['first_name', 'last_name',  'username', 'email','password1', 'password2']
        
        
    def clean_email(self):
        email= self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El mail ya esta registrado")
        return email