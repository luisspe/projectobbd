from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Productos, provedores


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'

class EntradasForm(forms.ModelForm):
    class Meta:
        model= Productos
        fields = ['unidadesEnStock']


class ProvedoresForm(forms.ModelForm):

    class Meta:
        model = provedores
        fields = '__all__'