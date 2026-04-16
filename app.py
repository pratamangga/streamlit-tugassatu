import streamlit as st

st.title("Sistem Rekomendasi HP Sederhana")
st.write("Sistem Cerdas menggunakan Streamlit | Angga Yoga Pratama - 2313010605")

# INPUT
budget = st.selectbox(
    "Pilih Budget:",
    ["< 2 Juta", "2 - 5 Juta", "> 5 Juta"]
)

kebutuhan = st.selectbox(
    "Pilih Kebutuhan:",
    ["Sosmed", "Gaming", "Fotografi"]
)

# BUTTON
if st.button("Dapatkan Rekomendasi"):

    if budget == "< 2 Juta" and kebutuhan == "Sosmed":
        st.success("Redmi, Realme, Vivo, Samsung")

    elif budget == "2 - 5 Juta" and kebutuhan == "Gaming":
        st.success("Iqoo, POCO X/F, Realme GT")

    elif budget == "> 5 Juta" and kebutuhan == "Gaming":
        st.success("Infinix GT, Tecno POVA")

    elif budget == "2 - 5 Juta" and kebutuhan == "Fotografi":
        st.success("Samsung, Iphone, Xiaomi, Motorola, Pixel")

    elif budget == "> 5 Juta" and kebutuhan == "Fotografi":
        st.success("Samsung, Iphone, Xiaomi, Motorola, Pixel")

    else:
        st.warning("Rekomendasi Belum Tersedia")
