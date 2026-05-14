from django.shortcuts import render
from .models import Palavra
from datetime import datetime
from django.shortcuts import redirect

def index(request):
    # 1. O dia do ano atual (ex: hoje é o dia 134 de 365)
    dia_do_ano = datetime.now().timetuple().tm_yday
    
    # 2. Quantas palavras existem no MySQL
    total_palavras = Palavra.objects.count()
    
    palavra_do_dia = None
    
    if total_palavras > 0:
        # 3. Lógica do Índice: O resto da divisão (%) garante que o número 
        # nunca seja maior que a quantidade de palavras que você tem.
        # Se você tem 1135 palavras, e hoje é o dia 134, ele pega a posição 134.
        index_palavra = dia_do_ano % total_palavras
        
        # 4. Busca a palavra naquela posição específica
        palavra_do_dia = Palavra.objects.all()[index_palavra]

    # 5. Entrega a "Palavra do Dia" para o HTML 
    return render(request, 'core/index.html', {'palavra': palavra_do_dia})

def salvar_configuracao(request):
    if request.method == 'POST':
        idioma_escolhido = request.POST.get('idioma')
        # Aqui no futuro salvaremos no perfil do usuário
        print(f"O usuário escolheu: {idioma_escolhido}")
        return redirect('index') # Volta para a tela inicial