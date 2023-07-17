from django.shortcuts import render, redirect
from contas.models import Contas
from ContasCategorias.models import Luz, Agua, Internet, PlanoDeSaude
from django.db.models import Q

def index(request):
    contas = (
        Contas
        .objects
        .all()    
    )


    return render(
        request,
        'contas/index.html',
        {
            'contas': contas,    
        }
    )

def luz(request):
    conta_luz = (
        Luz
        .objects
        .all()    
    )

    return render(
        request,
        'contas/contas_categorias/luz.html',
        {
            'luz': conta_luz,    
        }    
    )

def internet(request):
    conta_internet = (
        Internet
        .objects
        .all()    
    )

    return render(
        request,
        'contas/contas_categorias/internet.html',
        {
            'internet': conta_internet,    
        }    
    )

def agua(request):
    conta_agua = (
        Agua
        .objects
        .all()    
    )

    return render(
        request,
        'contas/contas_categorias/agua.html',
        {
            'agua': conta_agua,    
        }    
    )

def plano_de_saude(request):
    conta_plano = (
        PlanoDeSaude
        .objects
        .all()    
    )

    return render(
        request,
        'contas/contas_categorias/plano_de_saude.html',
        {
            'plano': conta_plano,    
        }    
    )

def search(request):
    search_value = request.GET.get('search', '').strip()

    if search_value == '':
        return redirect('index')

    contas = (
        Contas
        .objects
        .filter(
            Q(Nome_conta__icontains=search_value) |
            Q(vencimento__icontains=search_value) |
            Q(status__icontains=search_value) |
            Q(valor__icontains=search_value)
        )
    )

    return render(
        request,
        'contas/index.html',
        {
            'contas': contas,
            'search_value': search_value,
        }
    )

def handler404(request, exception):
    return render(request, 'contas/404.html', status=404)


def handler505(request, exception):
    return render(request, 'contas/505.html', status=505)