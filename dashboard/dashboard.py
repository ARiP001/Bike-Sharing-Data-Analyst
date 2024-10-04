import streamlit as st
import pandas as pd
import seaborn as sns
sns.set(style='dark')




st.title("Data Analisis pada Dataset Peminjaman Sepeda")
data_url = ".dashboard/main_data.csv"

data_df = pd.read_csv(data_url)
st.write("Ringkasan Statistik:")
st.dataframe(data_df.describe())

# Sidebar
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
