import datetime

from django.utils.timezone import *
from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    historial_medico = models.ForeignKey("historialMedico",  blank="true", null="true",on_delete= models.CASCADE,default=3, related_name="medico_historial")
    paciente = models.OneToOneField("Paciente", default=2, on_delete= models.CASCADE,related_name='paciente_medico')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    medico = models.ForeignKey("Medico", on_delete=models.CASCADE, blank="true", null="true", default=2, related_name="Paciente_medico")
    historial_medico = models.ForeignKey("historialMedico", on_delete = models.CASCADE, default=2, blank="true", null="true", related_name="historial_medico")
    pedido = models.ForeignKey("Pedido", on_delete = models.CASCADE, blank="true", default=3, null="true",related_name="pedido_paciente")
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class historialMedico(models.Model):
    paciente = models.ForeignKey("Paciente", default=1, on_delete=models.CASCADE)
    observaciones = models.TextField(max_length=300)
    medico = models.ForeignKey("Medico", on_delete=models.CASCADE, default=2 ,related_name="medico_historial")

    def __str__(self):
        return self.observaciones


class Turno(models.Model):
    fecha= models.DateTimeField(blank= False)
    medico = models.ForeignKey("Medico", on_delete=models.CASCADE, default=2 , related_name="medico_turno")
    paciente = models.ForeignKey("Paciente", on_delete=models.CASCADE, default=1, related_name="paciente_turno")

    def __str__(self):
        return self.fecha

class Pedido(models.Model):
    numero = models.IntegerField()
    estado = models.BooleanField()
    medio_de_pago = models.IntegerField()
    subtotal = models.DecimalField(max_digits= 5, decimal_places= 2, default=1)
    paciente = models.ForeignKey("Paciente", on_delete=models.CASCADE, default=1, related_name="pedido_paciente")
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE, default=2, related_name="producto_pedido")

    def __str__(self):
        return self.numero

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    imagen= models.ImageField(upload_to= "static/img", max_length= 200, height_field=None, width_field=None,null=True, blank= False)
    precio = models.DecimalField(max_digits= 5, decimal_places= 2)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=1, related_name="categoria_producto")
    imagen_producto = models.ImageField(upload_to='img/', default=1)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    es_lente = models.BooleanField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    nombre = models.CharField(max_length=30)
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Taller(models.Model):
    pedido = models.ForeignKey("Pedido", on_delete= models.CASCADE, default=1, blank= False)


class Gerencia(models.Model):
    paciente = models.ForeignKey("Paciente", on_delete=models.CASCADE)
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    ventas = models.ForeignKey("Venta", on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.