import streamlit as st
import streamlit_authenticator as stauth
from time import sleep


# exibir infos

if "nome1" in st.session_state and "cpf1" in st.session_state and "responsavel1" in st.session_state and "foto1" in st.session_state:
 st.header(f"nome: {st.session_state["nome1"]}")
 st.header(f"cpf: {st.session_state["cpf1"]}")
 st.header(f"responsavel: {st.session_state["responsavel1"]}")

if "foto1" in st.session_state:
    if st.session_state["foto1"] is not None:
        st.image(
            st.session_state["foto1"], caption="Foto do aluno", width=300
        )

import base64

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
    background_image_path = "img/fundo3.jpeg"  # Certifique-se de que o caminho está correto
    background_image = get_base64_image(background_image_path)

    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image}"); 
            background-size: cover;
            background-position: center; 
            background-attachment: fixed; 
        }}
    </style>
    """, unsafe_allow_html=True)


st.sidebar.image("img/vote.jpeg")
# Chamada da função para carregar o fundo
cadastro()

def ver_preenchidos(campos):
    return all(campos.values())
