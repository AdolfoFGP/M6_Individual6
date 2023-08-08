from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']'''


class RegistroUsuarioForm(UserCreationForm): 
    campos = (
        ('admin','admin'),
        ('usuario_comun', 'usuario_comun')
    )
    email = forms.EmailField(required=False)
    tipo_usuario = forms.ChoiceField(choices=campos)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario']