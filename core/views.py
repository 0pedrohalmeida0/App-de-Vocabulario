from django.shortcuts import render, redirect
from .models import Palavra
from datetime import datetime
from django.http import JsonResponse

def index(request):
    # --- NOVIDADE: Busca qual idioma foi salvo na sessão ---
    # Se for a primeira vez do usuário, ele assume 'pt-br' por padrão
    idioma_selecionado = request.session.get('idioma_foco', 'pt-br')

    # 1. O dia do ano atual (ex: hoje é o dia 134 de 365)
    dia_do_ano = datetime.now().timetuple().tm_yday
    
    # 2. ALTERAÇÃO: filtrar as palavras pelo idioma antes de contar
    palavras_do_idioma = Palavra.objects.filter(idioma=idioma_selecionado)
    total_palavras = palavras_do_idioma.count()
    
    palavra_do_dia = None
    
    if total_palavras > 0:
        # 3. Lógica do Índice: Agora baseada apenas nas palavras do idioma escolhido
        index_palavra = dia_do_ano % total_palavras
        
        # 4. Busca a palavra naquela posição específica dentro do filtro
        palavra_do_dia = palavras_do_idioma[index_palavra]

    # 5. Entrega a "Palavra do Dia" e o idioma atual para o HTML 
    # (Passar o idioma ajuda o HTML a manter o <select> marcado corretamente)
    context = {
        'palavra': palavra_do_dia,
        'idioma_selecionado': idioma_selecionado
    }
    return render(request, 'core/index.html', context)

def salvar_configuracao(request):
    if request.method == 'POST':
        idioma_escolhido = request.POST.get('idioma')
        
        # --- NOVIDADE: Agora, além do print, nós salvamos na sessão ---
        request.session['idioma_foco'] = idioma_escolhido
        
        print(f"O usuário escolheu e salvamos na sessão: {idioma_escolhido}")
        return redirect('index')
    
def api_palavra_do_dia(request):
    # Mesma lógica que você já validou
    idioma = request.session.get('idioma_foco', 'pt-br')
    palavras = Palavra.objects.filter(idioma=idioma)
    
    dia_do_ano = datetime.now().timetuple().tm_yday
    palavra = None
    
    if palavras.count() > 0:
        palavra = palavras[dia_do_ano % palavras.count()]
        
        # Retornamos apenas os dados, sem HTML
        dados = {
            'termo': palavra.termo,
            'significado': palavra.significado,
            'exemplo': palavra.exemplo,
            'idioma': palavra.idioma
        }
        return JsonResponse(dados)
    
    return JsonResponse({'erro': 'Nenhuma palavra encontrada'}, status=404)