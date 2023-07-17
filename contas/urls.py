from django.urls import path
from contas.views import index, search, luz, internet, agua, plano_de_saude

urlpatterns = [
    # Pagina inicial
    path('', index, name='index'),

    # Pagina de pesquisa
    path('search/', search, name='search'),
    
    # Pagina da luz
    path('categoria/Luz', luz, name='luz'),

    # Pagina da Internet
    path('categoria/Internet', internet, name='internet'),

    # Pagina da Agua
    path('categoria/Agua', agua, name='agua'),

    # Pagina do Plano+De+Saude
    path('categoria/Plano+De+Saude', plano_de_saude, name='plano'),
]
