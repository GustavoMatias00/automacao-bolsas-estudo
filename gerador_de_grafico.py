import pandas as pd
import plotly.express as px

print("Processando os dados para o dashboard interativo...")

# 1. Lemos o mesmo arquivo CSV de antes
df = pd.read_csv('noticias_bolsas_2026-05-26.csv', sep=';')

# 2. Preparamos os dados (o Plotly gosta dos dados organizados em tabelas)
contagem = df['Termo Buscado'].value_counts().reset_index()
contagem.columns = ['Faculdade', 'Quantidade de Notícias']

# 3. Criamos o gráfico interativo com visual moderno
fig = px.bar(
    contagem,
    x='Faculdade',
    y='Quantidade de Notícias', # O Plotly vai buscar essa coluna que criamos
    title='<b>Mapeamento de Bolsas de Estudo</b><br><sup>Volume de oportunidades por instituição na mídia</sup>',
    text='Quantidade de Notícias', # Coloca o número exato no topo de cada barra
    color='Quantidade de Notícias', # Faz a cor mudar dependendo do tamanho da barra
    color_continuous_scale='Teal', # Uma paleta de cores corporativa, elegante e moderna
    template='plotly_dark' # Fundo escuro e limpo
)

# 4. Ajustes finos de design (O "tapa no visual")
fig.update_traces(
    textposition='outside', # Número fica fora da barra para leitura mais clara
    marker_line_color='white', # Bordinha branca estilosa
    marker_line_width=1.5,
    textfont_size=14,
    hovertemplate="<b>%{x}</b><br>Notícias: %{y}<extra></extra>" # Customiza a caixinha ao passar o mouse
)

# Limpando poluição visual
fig.update_layout(
    title_font_size=22,
    xaxis_title="", # Remove o texto "Faculdade" de baixo (já está óbvio)
    yaxis_title="", # Remove o texto lateral 
    showlegend=False,
    margin=dict(t=100, b=50, l=50, r=50) # Dá um respiro nas margens
)

print("Gráfico pronto! Abrindo no seu navegador...")

# 5. Aqui acontece a mágica: ele abre o gráfico no Chrome/Edge!
fig.show()