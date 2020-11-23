from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('detalle_productos', views.detalle_productos, name="detalle_productos"),
    path('pedir_turnos',views.pedir_turnos, name="pedir_turnos")
]

# urlpatterns += staticfiles_urlpatterns()
