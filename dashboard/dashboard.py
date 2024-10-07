import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Path ke file CSV lokal
data_file = 'dashboard\main_data.csv' #ganti ke 'main_data.csv' jika ingin dijalankan di localhost

# Fungsi untuk memuat dataset
@st.cache_data
def load_data():
    try:
        # Baca dataset CSV
        df = pd.read_csv(data_file)

        # Hapus kolom 'No' jika ada
        if 'No' in df.columns:
            df = df.drop(['No'], axis=1)

        return df
    except FileNotFoundError:
        st.warning(f"File tidak ditemukan di path: {data_file}")
        return None

def tampilkan_peminjaman_per_musim(data):
    peminjaman_per_musim = data.groupby('season_x')[['casual_x', 'member_x']].sum().reset_index()

    colors = ['#FF9999', '#66B3FF'] 
    fig, ax = plt.subplots(figsize=(10, 6))

    peminjaman_per_musim.set_index('season_x').plot(kind='bar', stacked=True, color=colors, ax=ax)

    ax.set_title('Jumlah Peminjaman Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Peminjaman (dalam juta)')
    ax.legend(title='Tipe Peminjaman', labels=['Casual', 'Member'])
    ax.set_xticklabels(peminjaman_per_musim['season_x'], rotation=45)

    plt.tight_layout()
    st.pyplot(fig)

def plot_data_peminjaman(data):
    # Filter data untuk tahun 2011
    data_2011 = data[data['year_x'] == 0]
    data_per_bulan_2011 = data_2011.groupby('month_x').agg({
        'casual_x': 'sum',
        'member_x': 'sum',
        'count_x': 'sum'
    }).reset_index()
    
    data_per_bulan_2011['month_x'] = data_per_bulan_2011['month_x'].apply(lambda x: pd.to_datetime(f'2021-{x}-01').strftime('%B'))
    plt.figure(figsize=(12, 6))
    plt.plot(data_per_bulan_2011['month_x'], data_per_bulan_2011['casual_x'], label='Casual', marker='o', color='orange')
    plt.plot(data_per_bulan_2011['month_x'], data_per_bulan_2011['member_x'], label='Member', marker='o', color='blue')
    plt.plot(data_per_bulan_2011['month_x'], data_per_bulan_2011['count_x'], label='Total Peminjaman', marker='o', color='green')

    plt.title('Data Peminjaman 2011: Casual, Member, dan Total', size=20)
    plt.xlabel('Bulan', size=15)
    plt.ylabel('Jumlah Peminjaman', size=15)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

    # Filter data untuk tahun 2012
    data_2012 = data[data['year_x'] == 1]
    data_per_bulan_2012 = data_2012.groupby('month_x').agg({
        'casual_x': 'sum',
        'member_x': 'sum',
        'count_x': 'sum'
    }).reset_index()
    data_per_bulan_2012['month_x'] = data_per_bulan_2012['month_x'].apply(lambda x: pd.to_datetime(f'2021-{x}-01').strftime('%B'))
    plt.figure(figsize=(12, 6))
    plt.plot(data_per_bulan_2012['month_x'], data_per_bulan_2012['casual_x'], label='Casual', marker='o', color='orange')
    plt.plot(data_per_bulan_2012['month_x'], data_per_bulan_2012['member_x'], label='Member', marker='o', color='blue')
    plt.plot(data_per_bulan_2012['month_x'], data_per_bulan_2012['count_x'], label='Total Peminjaman', marker='o', color='green')

    plt.title('Data Peminjaman 2012: Casual, Member, dan Total', size=20)
    plt.xlabel('Bulan', size=15)
    plt.ylabel('Jumlah Peminjaman', size=15)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

def plot_temperature_vs_peminjaman(data):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=data, x='apparent_temperature_y', y='count_y', color='blue', alpha=0.7)
    sns.regplot(data=data, x='apparent_temperature_y', y='count_y', scatter=False, color='red')

    plt.title('Hubungan antara Apparent Temperature dan Jumlah Peminjaman per Hari')
    plt.xlabel('Suhu yang Terasa (berdasarkan skala dataset)')
    plt.ylabel('Jumlah Peminjaman')
    plt.grid()

    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

def angin_vs_peminjaman(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='windspeed_y', y='count_y', hue='windspeed_category', palette='Set2', s=100)
    plt.title('Clustering Kecepatan Angin dan Jumlah Peminjaman')
    plt.xlabel('Kecepatan Angin (berdasarkan skala dataset)')
    plt.ylabel('Jumlah Peminjaman')
    plt.grid(True)
    st.pyplot(plt) 

st.sidebar.title("Menu")
st.sidebar.markdown("[Perbandingan Casual dan Member](#perbandingan-pelanggan-casual-dan-member-tiap-musim)")
st.sidebar.markdown("[Grafik Peminjaman Perbulan](#grafik-peminjaman-perbulan)")
st.sidebar.markdown("[Pengaruh Suhu dan Total Peminjaman](#pengaruh-suhu-dan-total-peminjaman)")
st.sidebar.markdown("[Pengaruh Kecepatan angin dan Total Peminjaman](#pengaruh-kecepatan-angin-dan-total-peminjaman)")


st.write("# Analisis Data pada Dataset Penyewaan Sepeda")
data = load_data()

# Periksa apakah data berhasil dimuat
if data is not None:
    st.write("Berikut adalah beberapa baris dari dataset:")
    st.write(data.head())
else:
    st.error("Data gagal dimuat. Periksa path file CSV.")
st.write("Ekstensi _x adalah data dari dataset jam sedangkan _y adalah data dari dataset hari")

st.write("### Perbandingan Pelanggan Casual dan Member tiap Musim")
tampilkan_peminjaman_per_musim(data)
st.write("""
Analisis menunjukkan bahwa peminjam member mendominasi jumlah peminjaman sepeda dibandingkan peminjam kasual. Hal ini mengindikasikan bahwa member cenderung lebih sering menggunakan layanan ini.

Selain itu, musim panas (summer season) mencatat jumlah peminjaman tertinggi. Cuaca yang baik dan kegiatan luar ruangan selama musim ini mungkin menjadi faktor utama peningkatan peminjaman, serta menarik lebih banyak orang untuk bersepeda.
""")

st.write("### Grafik Peminjaman Perbulan")
plot_data_peminjaman(data)
st.write("""
Pada tahun pertama (2011), total peminjaman sepeda meningkat dari awal tahun hingga Mei, namun mulai menurun dari bulan Agustus hingga akhir tahun. Penurunan ini mungkin dipicu oleh perubahan musim dan aktivitas masyarakat yang berkurang.

Pada tahun kedua (2012), pola serupa terlihat dengan kenaikan peminjaman hingga September, diikuti oleh penurunan di bulan-bulan setelahnya.

Tidak ada perbedaan signifikan dalam pola antara peminjaman casual dan member; keduanya menunjukkan tren yang hampir identik, dengan kenaikan awal tahun dan penurunan setelahnya.
""")

st.write("### Pengaruh Suhu dan Total Peminjaman")
plot_temperature_vs_peminjaman(data)
st.write("""
Grafik scatter menunjukkan persebaran data antara suhu yang terasa (apparent temperature) dan jumlah peminjaman sepeda, dengan garis regresi yang mengindikasikan bahwa peningkatan suhu berhubungan dengan peningkatan jumlah peminjaman. Terdapat korelasi positif yang cukup signifikan dimana semakin tinggi suhu, semakin tinggi jumlah peminjaman sepeda. Ini menunjukkan bahwa peminjaman cenderung meningkat pada hari yang lebih hangat.
""")

st.write("### Pengaruh Kecepatan angin dan Total Peminjaman")
angin_vs_peminjaman(data)
st.write("""
Berdasarkan visualisasi persebaran data cenderung memadat pada kategori "Tenang" hingga "Berangin", ini menunjukkan bahwa jumlah peminjaman lebih banyak terjadi ketika kecepatan angin rendah atau sepoi-sepoi. Pada kondisi angin tersebut pengguna cenderung merasa lebih nyaman untuk bersepeda, yang berkontribusi pada tingginya jumlah peminjaman berulang. Sementara itu, saat kecepatan angin meningkat ke kategori "Angin Kencang," peminjaman berulang cenderung lebih sedikit, kemungkinan disebabkan oleh faktor ketidaknyamanan atau rasa tidak aman ketika bersepeda dalam kondisi cuaca yang lebih ekstrem. 

Hal ini dapat menunjukkan hubungan negatif antara kecepatan angin yang tinggi dan aktivitas peminjaman sepeda.
""")
