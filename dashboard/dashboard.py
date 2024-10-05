import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


data_file = r'./dashboard/main_data.csv'

@st.cache_data
def load_data():
    if os.path.isfile(data_file):
        df = pd.read_csv(data_file)

        if 'No' in df.columns:
            df = df.drop(['No'], axis=1)
          
        df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
        
        return df
    else:
        st.warning(f"File tidak ditemukan di path: {data_file}")
        return None
data = load_data()

if data is not None:
    st.write(data.head())
else:
    st.error("Data gagal dimuat. Periksa path file CSV.")


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
