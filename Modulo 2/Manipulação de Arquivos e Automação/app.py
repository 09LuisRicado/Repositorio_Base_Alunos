import streamlit as st

musicas = {
    "KayBlack": {
        "Bonjour": "https://youtu.be/jQSxSYeFKnE?si=ruB47IhJVRTYkrQ8",
        "Baila Linda": "https://youtu.be/d-JlYfbjHac?si=WEoNBL_5HACnWR2n",
    },
    "50 Cent": {
        "P.I.M.P": "https://youtu.be/Jy1D6caG8nU?si=2WG9EtmbANLRLxNk",
        "Many Men": "https://www.youtube.com/watch?v=5D3crqpClPY&list=RD5D3crqpClPY",
    },
    "Teto": {
        "Savana": "https://youtu.be/IH7PQvkn8mA?si=zsxnSLgW73cuE0V5"
    },
}
st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista",musicas.keys())
musicas_artistas = musicas[artista]

st.title(artista)
for musica in musicas_artistas.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)