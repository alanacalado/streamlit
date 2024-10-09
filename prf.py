import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Descubra seu tipo de pele",
    page_icon=":droplet:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Título e subtítulo com formatação
st.title("Qual é o seu tipo de pele?")
st.markdown("<h3 style='text-align: center;'>Descubra a rotina de cuidados ideal para você!</h3>", unsafe_allow_html=True)

# ... (resto do seu código)

# Exemplo de uso de colunas e imagens
col1, col2 = st.columns(2)

# Exemplo de uso de barra de progresso
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)


# Definição das perguntas
questoes = [
    {
        "questao": "Como você descreveria sua pele ao acordar?",
        "opcao": ["Oleosa", "Normal", "Seca", "Mista"]
    },
    {
        "questao": "Sua pele tende a ficar brilhante ao longo do dia?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Você tem tendência a acne?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Sua pele fica vermelha ou irritada facilmente?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Você sente sua pele seca ou áspera?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Você já notou áreas secas e descamativas na sua pele?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Sua pele se irrita com produtos cosméticos?",
        "opcao": ["Sim", "Não"]
    },
    {
        "questao": "Você tem alguma condição como rosácea ou eczema?",
        "opcao": ["Sim", "Não"]
    },
]

# Inicialização do aplicativo
st.title("Quiz de Tipo de Pele")
st.write("Responda as perguntas para descobrir qual é o seu tipo de pele.")

# Armazenar respostas
respostas = []

# Loop pelas questões
for index, questao in enumerate(questoes):
    resposta = st.radio(questao["questao"], questao["opcao"], key=index)
    respostas.append(resposta)

# Botão para calcular resultado
if st.button("Calcular Resultado"):
    score = {
        'normal': 0,
        'oleosa': 0,
        'seca': 0,
        'mista': 0,
        'acneica': 0,
        'rosacea': 0,
        'sensível': 0
    }

    # Avaliação das respostas
    if respostas[0] == "Oleosa":
        score['oleosa'] += 1
    elif respostas[0] == "Normal":
        score['normal'] += 1
    elif respostas[0] == "Seca":
        score['seca'] += 1
    elif respostas[0] == "Mista":
        score['mista'] += 1

    if respostas[1] == "Sim":
        score['oleosa'] += 1
    if respostas[2] == "Sim":
        score['acneica'] += 1
    if respostas[3] == "Sim":
        score['sensível'] += 1
    if respostas[4] == "Sim":
        score['seca'] += 1
    if respostas[5] == "Sim":
        score['seca'] += 1
    if respostas[6] == "Sim":
        score['sensível'] += 1
    if respostas[7] == "Sim":
        score['rosacea'] += 1

    # Determinando o tipo de pele
    resultado = ""
    if score['oleosa'] > 0:
        resultado += "Sua pele é oleosa."
    if score['seca'] > 0:
        resultado += " Sua pele é seca."
    if score['mista'] > 0:
        resultado += " Sua pele é mista."
    if score['acneica'] > 0:
        resultado += " Sua pele é acneica."
    if score['rosacea'] > 0:
        resultado += " Você pode ter rosácea."
    if score['sensível'] > 0:
        resultado += " Sua pele é sensível."

    if resultado == "":
        resultado = "Sua pele é normal."

    st.success(resultado)
