from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pelicula

@login_required
def home (request):
    return render(request,'home.html')

@login_required
def vistas(request):
    vistas=Pelicula.objects.order_by('fecha')
    return render(request,'vistas.html',{'vistas':vistas})

def register_vista(request):
    if request.method =='POST':
        pelicula=request.POST['pelicula']
        calificacion=request.POST['calificacion']
        comentario=request.POST['comentario']

        Pelicula.objects.create(pelicula=pelicula,calificacion=calificacion,comentario=comentario)
        return redirect('vistas')
    return render(request,'registrar_vista.html')

def delete_vista(request,id):
    vista=get_object_or_404(Pelicula,id=id)
    vista.delete()
    return redirect('vistas')

def update_vista(request,id):
    vista=get_object_or_404(Pelicula,id=id)

    if request.method =='POST':
        vista.pelicula=request.POST['pelicula']
        vista.calificacion=request.POST['calificacion']
        vista.comentario=request.POST['comentario']
        vista.save()
        return redirect('vistas')
    return  render(request,'actualizar_vista.html',{'vista':vista})
