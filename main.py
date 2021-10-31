import streamlit as st
import qrcode


st.set_page_config(
    page_title="Konversi Link - QrCode",
    initial_sidebar_state="expanded",
)


link = st.text_input("Masukkan link website : ")
img = qrcode.make(link)
# img.save("Link2.jpg")
st.image(img, caption='Link From')
