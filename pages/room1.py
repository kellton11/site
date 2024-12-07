import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep
from PIL import Image
import pandas as pd
import os

st.markdown("""
        <style>
            /*Estilo para o título */
            h1 {
                color: #FFFCCC;
                font-size: 30px;
                font-weight: bold;
            }

        .st-key-discurso1 button:hover {
            background-color: #F2C8AB;
            color: black;

            border: solid black;
        }
            
        .st-key-discurso2 button:hover {
            background-color: #F2C8AB;
            color: black;
            border: solid black;
            
        }
            
        .st-key-resultado button:hover {
            background-color: #F2C8AB;
            color: black;
            border: none;
            }

        .st-key-candidato1 button:hover{
            color: black;
            background-color: #A19E73;
            }
            
        .st-key-candidato2 button:hover{
            color: black;
            background-color: #A19E73;
            }

        .st-key-candidato1 button {
            \width: 260px;
            background-color: #777555;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            }

        .st-key-candidato2 button {
            \width: 260px;
            background-color: #777555;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            }

        .st-key-discurso1 button {
            \width: 260px;
            background-color: #776254;
            color: white;
            border-radius: 20px;
            padding: 10px 20px;
            border: solid;
            font-size: 18px;
            }

        .st-key-discurso2 button {
            \width: 260px;
            background-color: #776254;
            color: white;
            border-radius: 20px;
            padding: 10px 20px;
            border: solid;
            font-size: 18px;
            }

            justify-content: center;
            align: center;
        
        .st-key-resultado button {
            background-color: #C9A68E;
            color: black;
            }

        </style>
        </style>
            
        </style>    
            
    """, unsafe_allow_html=True)

caminho_arquivo = "dados.csv" 

def inicializar_csv(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        df = pd.DataFrame({
            "Candidato": ["Candidato 1", "Candidato 2"],
            "Votos": [0, 0]
        })
        df.to_csv(caminho_arquivo, index=False)

def registrar_voto(candidato, caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    df.loc[df['Candidatos'] == candidato, 'Votos'] += 1
    df.to_csv(caminho_arquivo, index=False)

# Títulos e descrição
st.title("🗳️ Sistema de Votação")

st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

st.write("")
st.write("")
st.write("")


# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou

col1, col2 = st.columns(2)

with col1:
    if st.button("Discurso do candidato 1", key='discurso1'):
        webbrowser.open("https://drive.google.com/file/d/11IVI3_s0NYogvjrYesEWxzz2KC7oO9Wv/view")
with col2:
        if st.button("Discurso do candidato 2",key='discurso2'):
            webbrowser.open("https://drive.google.com/file/d/1AZausUdYaAfLX70AU1VNTdWBbg1MxvQd/view")

if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Votar no Candidato 1", key='candidato1'):  
            registrar_voto("Candidato 1", "dados.csv")
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col4:
        if st.button("Votar no Candidato 2", key='candidato2'):
            registrar_voto("Candidato 2", "dados.csv")
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")             

votos_can_1 = []

col5, col6 = st.columns(2)
with col5:
    st.image("https://i.pinimg.com/736x/9a/1e/85/9a1e8537c653c89af975a05d2b8f2f6a.jpg", width=160)
with col6:
    st.image("https://media.tenor.com/UPiEUVO2Q04AAAAe/mulch-mulch-dog.png", width=160)

if st.button("Resultado",key='resultado', help="Ver resultado das eleições", use_container_width=True):
            sleep(0.5)
            st.success("Redirecionando...")
            st.switch_page("pages/resultado.py")

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
