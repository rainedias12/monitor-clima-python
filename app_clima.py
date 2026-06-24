import requests
import streamlit as st

# Configurações da página web
st.set_page_config(page_title="App de Clima", page_icon="☁️", layout="centered")

st.title("☁️ Monitor de Clima em Tempo Real")
st.markdown("Insira o nome de uma cidade para consultar as condições atuais.")

cidade = st.text_input("Digite o nome da cidade:", "Sao Paulo")

# USE A SUA CHAVE ATIVA AQUI
API_KEY = '792cae03ac92e8f43d2e9d468fb08586'  
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

if st.button("Consultar Clima"):
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        nome_cidade = dados['name']
        temp_celsius = dados['main']['temp'] - 273.15
        humidade = dados['main']['humidity']
        clima_em_ingles = dados['weather'][0]['main']
        
        traducao = {
            "Clear": "Céu Limpo", "Clouds": "Nublado", "Rain": "Chovendo",
            "Drizzle": "Chuva Leve", "Thunderstorm": "Tempestade", 
            "Snow": "Neve", "Mist": "Névoa"
        }
        clima_pt = traducao.get(clima_em_ingles, clima_em_ingles)
        
        st.success(f"Dados carregados para {nome_cidade}!")
        
        # Criação dos cards visuais
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="🌡️ Temperatura", value=f"{temp_celsius:.1f} °C")
        with col2:
            st.metric(label="💧 Umidade", value=f"{humidade} %")
        with col3:
            st.metric(label="☁️ Condição", value=clima_pt)
            
    else:
        st.error(f"Não foi possível encontrar a cidade '{cidade}'.")