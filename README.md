# 📊 Analisis Sentimen Ulasan Aplikasi Ruangguru menggunakan Deep Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-orange)
![Deep Learning](https://img.shields.io/badge/Model-LSTM%20%26%20GRU-success)

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi pemrosesan bahasa alami (NLP) untuk menganalisis sentimen ulasan pengguna terhadap platform *EdTech* Ruangguru di Google Play Store. Proyek ini bertujuan untuk mengekstrak wawasan mengenai pengalaman pengguna (*User Experience*) guna memahami *pain points* serta kepuasan pelajar saat menggunakan aplikasi pembelajaran digital.

Model *Deep Learning* yang dikembangkan dalam proyek ini mampu mengklasifikasikan teks ulasan ke dalam tiga kategori sentimen: **Positif, Netral, dan Negatif**.

## ✨ Fitur Utama
- **Data Scraping Mandiri:** Mengumpulkan lebih dari 10.000 ulasan secara langsung dari Google Play Store menggunakan `google-play-scraper`.
- **Penanganan Imbalanced Data:** Menggunakan teknik Oversampling (RandomOverSampler) untuk memastikan distribusi kelas sentimen seimbang sebelum pelatihan model.
- **Eksperimen Arsitektur Multi-Skema:** Melakukan 3 skema pelatihan berbeda untuk membandingkan performa model:
  1. **Skema 1:** LSTM (Split Latih/Uji 80:20)
  2. **Skema 2:** GRU (Split Latih/Uji 80:20)
  3. **Skema 3:** LSTM (Split Latih/Uji 90:10)
- **Akurasi Tinggi:** Mencapai akurasi testing di atas **96%** menggunakan arsitektur LSTM dengan optimasi lapisan `Dropout` dan *pre-padding* urutan teks.

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python
- **Framework Model:** TensorFlow / Keras
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning Utilities:** Scikit-Learn, Imbalanced-Learn
- **Scraping Tool:** Google Play Scraper

## 📂 Struktur Repositori
```text
├── dataset_ruangguru.csv              # Dataset ulasan hasil scraping (>10.000 baris)
├── scraping_ruangguru.py              # Script Python untuk mengambil data dari Play Store
├── Proyek_Analisis_Sentimen_Ruangguru.ipynb  # Notebook utama berisi preprocessing, pelatihan, & evaluasi model
├── requirements.txt                   # Daftar dependensi library untuk menjalankan proyek
└── README.md                          # Dokumentasi proyek
