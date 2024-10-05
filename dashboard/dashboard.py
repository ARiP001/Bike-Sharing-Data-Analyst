import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from io import StringIO

uploaded_file = st.file_uploader("main_data.csv")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


# # Periksa apakah data berhasil dimuat
# if data is not None:
#     st.write(data.head())  # Tampilkan beberapa baris pertama dari dataset
# else:
#     st.error("Data gagal dimuat. Periksa path file CSV.")


# Sidebar navigasi
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Subheader 1](#subheader-1)")
st.sidebar.markdown("[Subheader 2](#subheader-2)")
st.sidebar.markdown("[Subheader 3](#subheader-3)")

# Konten Utama
st.write("## Konten Utama")
st.write("Ini adalah artikel panjang yang menjelaskan berbagai hal. Silakan gulir ke bawah atau gunakan navigasi di sidebar untuk pergi ke subheader yang diinginkan.")

# Subheader 1
st.write("## Subheader 1")
st.write("""
Ini adalah konten untuk Subheader 1. Anda bisa menambahkan informasi, data, atau penjelasan lebih lanjut di sini.
""")

# Subheader 2
st.write("## Subheader 2")
st.write("""
Ini adalah konten untuk Subheader 2. Konten ini bisa menjelaskan topik lain yang relevan dengan artikel.
""")

# Subheader 3
st.write("## Subheader 3")
st.write("""
Ini adalah konten untuk Subheader 3. Di sini Anda dapat menyampaikan informasi tambahan atau ringkasan tentang apa yang telah dibahas.
""")
