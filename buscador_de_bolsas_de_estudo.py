import urllib.parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def buscar_noticias(termo_busca):
    """
    Função que busca notícias no Google News via RSS com base em um termo específico.
    Usamos o RSS porque é uma forma estruturada e legalizada de ler as notícias,
    evitando que o nosso script seja bloqueado pelo site.
    """
    print(f"Buscando novidades para: '{termo_busca}'...")
    
    # Codifica o termo de busca para o formato de URL (ex: "bolsa PUC" vira "bolsa%20PUC")
    termo_codificado = urllib.parse.quote(termo_busca)
    
    # URL do feed RSS do Google News focado no Brasil (pt-BR)
    url = f"https://news.google.com/rss/search?q={termo_codificado}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    try:
        # Faz a requisição (visita o site)
        resposta = requests.get(url)
        # Verifica se a requisição deu certo (código 200)
        resposta.raise_for_status()
        
        # Transforma o texto XML/HTML recebido em um objeto BeautifulSoup para facilitar a leitura
        soup = BeautifulSoup(resposta.content, features="xml")
        
        # Encontra todos os itens de notícia ('item' no padrão RSS)
        noticias = soup.findAll('item')
        
        resultados = []
        # Vamos pegar no máximo as 5 notícias mais recentes de cada termo
        for noticia in noticias[:5]:
            titulo = noticia.title.text
            link = noticia.link.text
            data_publicacao = noticia.pubDate.text
            
            resultados.append({
                'Termo Buscado': termo_busca,
                'Título': titulo,
                'Data': data_publicacao,
                'Link': link
            })
            
        return resultados
        
    except Exception as e:
        print(f"Erro ao buscar '{termo_busca}': {e}")
        return []

def main():
    # Aqui colocamos as suas palavras-chave de interesse!
    # Incluí as faculdades que você deseja prestar vestibular.
    termos_de_interesse = [
        "bolsa de estudo faculdade",
        "vestibular CEDERJ",
        "bolsas de estudo Unisuam",
        "isenção vestibular UERJ",
        "bolsa PUC Rio",
        "Prouni vagas"
    ]
    
    todas_as_noticias = []
    
    print("Iniciando o robô buscador de bolsas de estudo...\n")
    
    # Percorre cada termo e faz a busca
    for termo in termos_de_interesse:
        noticias_encontradas = buscar_noticias(termo)
        todas_as_noticias.extend(noticias_encontradas)
    
    # Se encontrou alguma notícia, vamos exibir e salvar em um arquivo CSV
    if todas_as_noticias:
        print("\n--- RESUMO DAS NOTÍCIAS ENCONTRADAS ---")
        for i, noticia in enumerate(todas_as_noticias, 1):
            print(f"{i}. {noticia['Título']}")
            print(f"   Link: {noticia['Link']}\n")
            
        # Transformando a lista de dicionários em um DataFrame do Pandas (base para Data Science/Machine Learning)
        df = pd.DataFrame(todas_as_noticias)
        
        # Nome do arquivo com a data atual
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"noticias_bolsas_{data_hoje}.csv"
        
        # Salva o arquivo CSV no seu computador (sem o índice na lateral)
        df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
        
        print(f"\nSucesso! As notícias foram salvas na planilha: {nome_arquivo}")
        print("Você pode abrir este arquivo no Excel ou no Google Sheets para organizar suas opções.")
    else:
        print("Nenhuma notícia recente foi encontrada hoje.")

# Essa estrutura garante que o script só rode quando executado diretamente
if __name__ == "__main__":
    main()