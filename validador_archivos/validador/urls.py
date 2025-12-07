from django.urls import path
from .views import validar_archivo

urlpatterns = [
    path('', validar_archivo, name='validar'),
]
