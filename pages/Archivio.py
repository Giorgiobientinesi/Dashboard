import streamlit as st

st.markdown('<h1 style="color: #;">Archivio Finanza</h1>',
            unsafe_allow_html=True)
st.write(" ")
col1,col2 = st.columns(2)



with open('pages/Portafogli.zip', 'rb') as f:
   col1.download_button('Portafogli', f, file_name='archive.zip')



with open('pages/Codici.zip', 'rb') as f:
   col2.download_button('Codici', f, file_name='archive.zip')