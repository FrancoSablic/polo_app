from django.contrib import admin
from .models import Medico, Paciente, historialMedico, Turno, Pedido, Producto, Categoria, Taller, Venta

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(historialMedico)
admin.site.register(Turno)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Taller)
admin.site.register(Venta)