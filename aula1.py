import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos?regiao=norte&ano=2022"
response = requests.get(url)
# json
# dicionário
# DataFrame
df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.metric('Receita',df['Preço'].sum())
    st.metric('Quantidade de vendas (linhas)',df.shape[0])
    st.metric('Quantidade de variáveis (colunas)', df.shape[1])
    st.dataframe(df)
else:
    st.write("Clique no botão todos")