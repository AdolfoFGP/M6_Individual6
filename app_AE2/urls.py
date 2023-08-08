from django.urls import path
from . import views

app_name = 'app_AE2'

urlpatterns = [
    path("", views.landing, name='landing'),
]