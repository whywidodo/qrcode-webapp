import streamlit as st
import qr_maker

st.title('QRCode Generator')

hyper_link = st.text_input("Tuliskan link :",
                           "https://www.google.com")

qr_size = st.slider('Perbesar ', min_value=6, max_value=12, value=6)
st.write("Ukuran", qr_size)

# (3.1) without logo
qr_name = qr_maker.qr_code(link=hyper_link, logo=False, size=qr_size)
st.image(qr_name, caption='Gambar QRCode')
