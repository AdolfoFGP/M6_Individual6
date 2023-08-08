from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_AE3/usuarios.html', {'usuarios': usuarios})
