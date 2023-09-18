import streamlit as st


st.title("Encuesta :) ")

st.write("selecciona un objeto que tenga este color o parecido")
st.image("verde.png", use_column_width=True)


option = st.selectbox('Selecciona tu opción',
    ("palta", "arbol", "rana", "manzana"))
if option == "palta":
  st.write("gracias por responder :)")

elif option == "arbol":
  st.write("gracias por tu respuesta :)")

elif option == "rana":
  st.write("gracias por colaborar en la encuesta :)")
else:
  st.write("muchas gracias por responder :)")
    
    
    


