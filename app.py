import streamlit as st

# Título da aplicação
st.title("Meu Primeiro Projeto com Streamlit")

# Texto de introdução
st.write("Bem-vindo ao meu primeiro app usando Streamlit!")

# Entrada do usuário
nome = st.text_input("Qual é o seu nome?")

# Botão para exibir mensagem
if st.button("Enviar"):
    st.write(f"Olá, {nome}! Obrigado por usar este app.")