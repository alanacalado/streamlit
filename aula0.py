import streamlit as st

st.write("Alô mundo")


#Estamos iniciando o streamlit
#Ele nos ajudará no projeto final
#Em sua instalação vem incluido o pandas e outras libs


idade = st.number_input("Digite sua idade:", min_value=14, max_value=120)
if idade >= 18:
    #uso obrigatório de identação
    st.write(f"Alô Mundo - Você é maior de idade: {idade}")
else:
    st.write(f"Alô Mundo - Você é menor de idade: {idade}")