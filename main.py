import streamlit as st
import qrcode

st.title('QRCode Generator')

hyper_link = st.text_input("Tuliskan link :", "https://www.google.com")

qr_size = st.slider('Perbesar ', min_value=6, max_value=12, value=6)
st.write("Ukuran", qr_size)
