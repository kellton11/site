import streamlit as st

if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

# Estilo personalizado
st.markdown("""
    <style>
        body {
            background-color: #f9fbfd;
        }
        h1 {
            color: #356abb;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color:#628af0 ;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: ;
        }
        .feedback-box {
            background-color: #eef7ff;
            border: 1px solid #cce5ff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feedback-box h6 {
            color: #5c85d6;
            margin: 0 0 5px 0;
            font-weight: bold;
        }
        .feedback-box p {
            color: #333;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 Feedbacks")

st.write("")
st.write("")

name = st.text_input("Digite seu nome:")
feedback = st.text_area("Deixe seu feedback:")
st.success("Obrigado pelo seu feedback!")

genre = st.radio(
    "Como você avalia nosso site?",
    ["⭐", "***⭐⭐***", "⭐⭐⭐", "⭐⭐⭐⭐", "🌟🌟🌟🌟🌟"],
    index=None,
)


st.write("voce selecionou:", genre)

if st.button("Enviar"):
    if feedback:
        st.session_state.feedback_list.append({"name": name or "Anônimo", "feedback": feedback})
    else:
        st.warning("Por favor, insira seu feedback antes de enviar.")

st.write("---")
st.subheader("📋 Feedbacks Recebidos:")


if st.session_state.feedback_list:
    for fb in st.session_state.feedback_list:
        st.markdown(f"""
            <div class="feedback-box">
                <h6>{fb["name"]}</h6>
                <p>{fb["feedback"]}</p>
                <p> Avaliou com {genre} estrelas! </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("Nenhum feedback recebido ainda.")

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
