import os
import django

# 1. Configura o ambiente do Django para o script funcionar fora do servidor
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup_projeto.settings')
django.setup()

# Importar o Model depois do setup do Django
from core.models import Palavra

def importar_do_txt(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return

    palavras_criadas = 0

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split('|')
            
            if len(partes) == 4:
                termo, significado, exemplo, idioma = partes
                
                # Agora incluímos o idioma no critério de busca
                obj, created = Palavra.objects.get_or_create(
                    termo=termo,
                    idioma=idioma, # O idioma entra aqui para diferenciar a busca
                    defaults={'significado': significado, 'exemplo': exemplo}
                )
                
                if created:
                    palavras_criadas += 1   
                    print(f"Adicionada: {termo}")

    print(f"\nSucesso! {palavras_criadas} novas palavras foram carregadas no MySQL.")

if __name__ == "__main__":
    importar_do_txt('palavras.txt')