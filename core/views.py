from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core.models import Avaluos, Clientes, Tipos, Estatus, Valuadores, Estados, Municipios, Colonias
# Create your views here.

def home(request):
    return render(request,'core/home.html')

def prueba(request):
    servs = Avaluos.objects.all()[0:19]
    prueba_list=[]
    for serv in servs:
        prueba='Ubicación : '
        if len(list(serv.calle))>0: #is not None and serv.calle != '':
            prueba += 'Calle : ' + serv.calle
        if len(list(serv.numero))>0: #is not None and serv.numero != '':
            prueba += 'Número : ' + serv.numero
        if len(list(serv.manzana))>0: #is not None and serv.manzana != '':
            prueba += 'Manzana : ' + serv.manzana
        prueba_list.append([serv.avaluoid,prueba,serv.dtsolicitud,serv.estatusid])   
    
    return render(request,'core/prueba.html',{'prueba_list': prueba_list})


@login_required
def servicios(request):
    servs = Avaluos.objects.all()[:19]
    clientes = Clientes.objects.order_by('nombre')
    tipos = Tipos.objects.order_by('display')
    valuadores = Valuadores.objects.order_by('display')
    estatus = Estatus.objects.order_by('nombre')
    estados = Estados.objects.order_by('nombre')
    iterador = []
    for serv in servs:
        ubicacion=''
        if len(list(serv.calle))>0: #is not None or serv.calle != '':
            ubicacion += 'Calle : ' + serv.calle + ', '
        if len(list(serv.numero))>0: #is not None or serv.numero != '':
            ubicacion += 'Número : ' + serv.numero + ', '
        if len(list(serv.manzana))>0: #is not None or serv.manzana != '':
            ubicacion += 'Manzana : ' + serv.manzana + ', '
        iterador.append([serv.avaluoid,ubicacion,serv.dtsolicitud,serv.estatusid])  
        
    return render(request,'core/servicios.html',{
        'servs': servs, 
        'clientes': clientes, 
        'tipos': tipos,
        'valuadores': valuadores,
        'estatus': estatus,
        'estados': estados,
        'ubicacion': ubicacion,
        'iterador' : iterador,
        })

def get_estados(request):
    estados = list(Estados.objects.values().order_by('nombre'))
    if (len(estados)>0):
        data = {
            "message": "Success", 
            "estados": estados}
    else:
        data = {"message": "Not Found"}
    
    return JsonResponse(data)



def get_municipios(request,estadoid):
    municipios = list(Municipios.objects.filter(estadoid=estadoid).values().order_by('nombre'))
    if (len(municipios)>0):
        data = {
            "message": "Success", 
            "estados": municipios}
    else:
        data = {"message": "Not Found"}
    
    return JsonResponse(data)


def get_colonias(request,municipioid):
    municipios = list(Colonias.objects.filter(municipioid=municipioid).values().order_by('nombre'))
    if (len(municipios)>0):
        data = {
            "message": "Success", 
            "municipios": municipios}
    else:
        data = {"message": "Not Found"}
    
    return JsonResponse(data)
    


def exit(request):
    logout(request)
    return redirect('home')

