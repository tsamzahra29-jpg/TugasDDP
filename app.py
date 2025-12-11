import streamlit as st

st.set_page_config(page_title="Bangun Datar", page_icon="📐")
st.title("Aplikasi perhitungan bangun datar")
st.write("Silahkan pilih menu di samping untuk memulai")

def luas_persegi(sisi):
    return sisi * sisi
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari
#Sidebar
menu = st.sidebar.selectbox("Pilih bagun datar",("Luas Persegi", "Luas Segitiga", "Luas Lingkaran"))

if menu == "Luas Persegi":
    st.header("Luas Persegi")
    st.image("https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg.webp", caption = "Rumus Luas Persegi", width = 400)
    #input
    sisi = st.number_input("Masukkan panjang persegi", min_value=0)
    if st.button("Hitung"):
        luas = luas_persegi (sisi)
        st.write(f"Luas Persegi dengan sisi {sisi} adalah {luas}")
elif menu == "Luas Segitiga":
    st.header("Luas Segitiga")
    st.image("https://media.suara.com/pictures/970x544/2021/11/11/76640-rumus-luas-segitiga-jadijuaracom.jpg", caption = "Rumus Luas Segitiga", width = 400)
    #Input
    alas = st.number_input("Masukkan panjang alas segitiga", min_value=0)
    tinggi = st.number_input("Masukkan panjang tinggi segitiga", min_value=0)
    if st.button("Hitung"):
        luas = luas_segitiga(alas, tinggi)
        st.write(f"Luas Segitiga dengan alas{alas} dan tinggi{tinggi} adalah {luas}")
elif menu == "Luas Lingkaran":
    st.header("Luas Lingkaran")
    st.image("https://i.pinimg.com/736x/e3/ec/fc/e3ecfc747bbfe1186aa4992e19ea8596.jpg", caption = "Rumus Luas Lingkaran", width = 400)
    #Input
    jari_jari = st.number_input("Masukkan panjang jari-jari lingkaran", min_value=0)
    if st.button("Hitung"):
        luas = luas_lingkaran(jari_jari)
        st.write(f"Luas Lingkaran dengan jari-jari{jari_jari}adalah {luas}")


