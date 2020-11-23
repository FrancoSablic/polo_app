from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'/admin')

def index(request):
    return render(request,'polo_app/index.html')

def productos(request):
    return render(request,'polo_app/productos.html')

def detalle_productos(request):
    return render(request,'polo_app/detalle_productos.html')

def pedir_turnos(request):
    return render(request,'polo_app/pedir_turnos.html')

def contacto(request):
    return render(request,'polo_app/contacto.html')

