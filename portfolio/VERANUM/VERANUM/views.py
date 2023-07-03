from django.shortcuts import render





# Create your views here.

def home(request):
    return render(request, 'index.html')


def pag_registro(request):
    return render(request, 'registro.html')


def ini_sesion(request):
    return render(request, 'ini_sesion.html')