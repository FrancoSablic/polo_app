from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('detalle_productos', views.detalle_productos, name='detalle_productos'),
    path('pedir_turnos',views.pedir_turnos, name='pedir_turnos'),
    path('contacto', views.contacto, name='contacto'),
]

