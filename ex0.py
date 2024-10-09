# importe o streamlit

# entre com um número

# verifique se o número é positivo, negativo ou nulo 

import streamlit as st

num = st.number_input("Digite um número :")
if num >= 1:
    
    st.write(f"Número positivo: {num}")
elif num <= -1:
     st.write(f"Número negativo: {num}")

else:
    st.write(f"Número nulo : ")