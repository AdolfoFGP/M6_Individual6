from django.shortcuts import render

def landing(request):
    return render(request, 'app_AE2/landing.html', {'saludo':'Bienvenido al landing page'})
# Create your views here.
