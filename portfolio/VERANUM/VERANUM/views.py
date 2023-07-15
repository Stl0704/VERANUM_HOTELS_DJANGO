from django.shortcuts import render, redirect
from reservas.models import Usuario , Platillo
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    return render(request, 'index.html')

def pag_registro_inicio(request):
    return render(request, 'logsignin.html')


def reserva (request):
    return render (request, 'reserva.html')


# LISTAR PLATILLOS 

def restaurante(request):
    listaPlatillos = Platillo.objects.all()
    ctx = {'platillo': listaPlatillos}
    return render(request, 'restaurante.html', ctx)


# FUNCIONES REGISTRO INICIO SESION




def pag_registro_inicio(request):
    if request.method == 'POST':
        if 'logemail' in request.POST and 'logpass' in request.POST:
            # Inicio de sesión
            email = request.POST['logemail']
            contrasenia = request.POST['logpass']
            user = authenticate(request, username=email, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('inicio')
        else:
            # Registro
            nombreu = request.POST['nombreu']
            rut = request.POST['rut']
            fNac = request.POST['fnac']
            email = request.POST['email']
            contrasenia = request.POST['contrasenia']
            direccion = request.POST['direccion']

            usuario = Usuario(
                nombreu=nombreu,
                rut=rut,
                fNac=fNac,
                email=email,
                contrasenia=contrasenia,
                direccion=direccion
            )
            usuario.save()

            return redirect('inicio-sesion')

    return render(request, 'logsignin.html')