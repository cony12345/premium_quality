import streamlit as st
import random
import cachipun 
st.title("Bienvenido al Cachipun 😂 ")
st.markdown("#### **Piedra Papel o Tijera**")
st.write("Para jugar, por favor selecciona: piedra, papel o tijera.")

options = ["Piedra", "Papel", "Tijera"]
pc_opt = random.choice(options)

option = st.selectbox('Selecciona tu opción',
    ('Piedra', 'Papel', 'Tijera'))

st.write('La computadora ha seleccionado:', pc_opt)

st.markdown(f"### {cachipun.result(pc_opt, option)}")
