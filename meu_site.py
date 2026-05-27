import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração inicial da página
st.set_page_config(page_title="Radar de Bolsas Pro", page_icon="🎓", layout="wide")

# =========================================================================
# O TRIO ENTRANDO EM AÇÃO: INJETANDO HTML E CSS NO STREAMLIT
# =========================================================================
st.markdown("""
    <style>
    /* Customizando o fundo principal da aplicação */
    .stApp {
        background-color: #0d0f12;
    }
    
    /* Criando uma classe CSS para cartões de notícias estilizados */
    .cartao-noticia {
        background-color: #161b22;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #00f2fe; /* Bordinha neon futurista */
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Estilizando o título dentro do cartão HTML */
    .titulo-noticia {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 8px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Estilizando os metadados (Data e Link) */
    .meta-noticia {
        color: #8b949e;
        font-size: 12px;
    }
    
    .meta-noticia a {
        color: #58a6ff;
        text-decoration: none;
        font-weight: bold;
    }
    
    .meta-noticia a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)
# =========================================================================

# Cabeçalho do Site usando HTML estrutural simples para o título
st.markdown('<h1 style="color: #ffffff; font-family: sans-serif;">🎓 Radar de Bolsas de Estudo</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #8b949e;">Painel analítico integrado com extração de dados e estilização customizada.</p>', unsafe_allow_html=True)
st.divider()

try:
    # Lendo a planilha gerada pelo seu robô buscador
    df = pd.read_csv('noticias_bolsas_2026-05-26.csv', sep=';')
    
    # Dividindo a tela em colunas de tamanhos diferentes (Gráfico maior, lista menor)
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<h3 style="color: #ffffff;">📊 Gráfico de Oportunidades</h3>', unsafe_allow_html=True)
        
        contagem = df['Termo Buscado'].value_counts().reset_index()
        contagem.columns = ['Faculdade', 'Quantidade de Notícias']

        # Gráfico interativo com a paleta de cores combinando com o site
        fig = px.bar(
            contagem,
            x='Faculdade',
            y='Quantidade de Notícias',
            color='Quantidade de Notícias',
            color_continuous_scale=['#161b22', '#00f2fe'], # Gradiente combinando com o CSS
            template='plotly_dark'
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_title="",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<h3 style="color: #ffffff;">📑 Feed de Notícias Estilizado</h3>', unsafe_allow_html=True)
        
        # Criando uma área rolável para as notícias usando HTML/CSS
        st.markdown('<div style="max-height: 450px; overflow-y: auto; padding-right: 10px;">', unsafe_allow_html=True)
        
        # O Python percorre a planilha e monta blocos de código HTML puro para cada linha!
        for index, linha in df.iterrows():
            st.markdown(f"""
                <div class="cartao-noticia">
                    <div class="titulo-noticia">{linha['Título']}</div>
                    <div class="meta-noticia">
                        📅 {linha['Data']} | 🌐 <a href="{linha['Link']}" target="_blank">Acessar Notícia</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

except FileNotFoundError:
    st.error("Planilha não encontrada! Certifique-se de rodar o buscador primeiro.")