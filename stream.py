import streamlit as st


st.title("Encuesta :) ")

st.write("selecciona un objeto que tenga este color")
st.image("verde.png", use_column_width=True)


option = st.selectbox('Selecciona tu opción',
    ("palta", "arbol", "rana", "manzana"))

if option == "palta":
    st.write ("Gracias por responder :)")
else: 
    st.write("Gracias por responder :)")
    
    


