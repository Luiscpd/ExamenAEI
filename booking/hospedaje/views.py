
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import CreateHuesped

# Create your views here.

def index(request):
    title = 'Bienvenido a Maya Hotel'
    return render(request, 'index.html', {
        'title': title
    })

def datos_huesped(request):
    if request.method == 'GET':
        return render(request, 'datos_huesped.html', {
            'form': CreateHuesped()
        })
    else:
        DatosHuesped.objects.create(DPI=request.POST["DPI"])
        DatosHuesped.objects.create(name=request.POST["name"])
        DatosHuesped.objects.create(last_name=request.POST["last_name"])
        return redirect('index')