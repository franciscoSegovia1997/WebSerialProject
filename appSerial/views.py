from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import usuarioSistema, dispositivoSistema

# Create your views here.
def index(request):
    return render(request,'index.html')

def crearUsuario(request):
    if request.method == 'POST':
        datos = json.load(request)
        nombreUsuario = datos.get('nombreUsuario')
        apellidoUsuario = datos.get('apellidoUsuario')
        edadUsuario = datos.get('edadUsuario')
        profesionUsuario = datos.get('profesionUsuario')
        usuarioSistema.objects.create(
            nombreUsuario=nombreUsuario,
            apellidoUsuario=apellidoUsuario,
            edadUsuario=edadUsuario,
            profesionUsuario=profesionUsuario
        )
        return JsonResponse({
            'resp':'ok'
        })
    
def consultarUsuarios(request):
    usuariosTotales = usuarioSistema.objects.all().order_by('id')
    usuariosSistema = []
    for usuarioInfo in usuariosTotales:
        usuariosSistema.append({
            'id':usuarioInfo.id,
            'nombreUsuario':usuarioInfo.nombreUsuario,
            'apellidoUsuario':usuarioInfo.apellidoUsuario,
            'edadUsuario':usuarioInfo.edadUsuario,
            'profesionUsuario':usuarioInfo.profesionUsuario
        })
    return JsonResponse({
        'usuariosSistema':usuariosSistema
    })

def consultarDispositivos(request):
    dispositivosTotales = dispositivoSistema.objects.all().order_by('id')
    dispositivosSistema = []
    for dispositivoInfo in dispositivosTotales:
        dispositivosSistema.append({
            'id':dispositivoInfo.id,
            'nombreDispositivo':dispositivoInfo.nombreDispositivo,
            'codigoDispositivo':dispositivoInfo.codigoDispositivo,
            'fabricanteDispositivo':dispositivoInfo.fabricanteDispositivo,
        })
    return JsonResponse({
        'dispositivosSistema':dispositivosSistema
    })

def crearDispositivo(request):
    if request.method == 'POST':
        datos = json.load(request)
        nombreDispositivo = datos.get('nombreDispositivo')
        codigoDispositivo = datos.get('codigoDispositivo')
        fabricanteDispositivo = datos.get('fabricanteDispositivo')
        dispositivoSistema.objects.create(
            nombreDispositivo=nombreDispositivo,
            codigoDispositivo=codigoDispositivo,
            fabricanteDispositivo=fabricanteDispositivo,
        )
        return JsonResponse({
            'resp':'ok'
        })