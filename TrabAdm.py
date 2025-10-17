# importar as bibliotecas
import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(
    page_title="Relatório BYD",
    layout="centered"
)

# Título e subtítulo
st.write("""
# Relatório BYD

Integrantes do Grupo:  
**Andressa Rocha, Julia Dias, Marcelo Uchôa, Miguel da Costa, Gabriel Yuzo, Felipe Beltrão, Enzo Velasco e Cássio Azevedo**
""")

# Seções do relatório
st.subheader("1. Descrição da Organização")
st.subheader("2. Ambiente Contextual e Operacional")
st.subheader("3. Cultura Organizacional e Gestão")
st.subheader("4. Estratégias de Adaptação ao Ambiente")
st.subheader("5. Mapa de Stakeholders")
