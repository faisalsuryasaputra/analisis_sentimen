from google_play_scraper import Sort, reviews
import pandas as pd
import time

# Konfigurasi Scraping
app_id = 'com.ruangguru.livestudents'
target_count = 12000 # Target ulasan yang ingin diambil
all_reviews = []
continuation_token = None

print(f"Memulai proses scraping untuk aplikasi {app_id}...")

# Looping untuk mengambil data secara bertahap
while len(all_reviews) < target_count:
    try:
        result, continuation_token = reviews(
            app_id,
            lang='id',          
            country='id',       
            sort=Sort.NEWEST,   
            count=1000,         
            continuation_token=continuation_token
        )
        
        if not result:
            print("Tidak ada ulasan baru yang ditemukan. Proses berhenti.")
            break
            
        all_reviews.extend(result)
        print(f"Berhasil mengumpulkan {len(all_reviews)} ulasan...")
        
        # Berhenti jika token habis 
        if continuation_token is None:
            print("Mencapai akhir ulasan di server. Proses berhenti.")
            break
            
        # Jeda 1 detik agar aktivitas scraping tidak diblokir Google
        time.sleep(1) 
        
    except Exception as e:
        print(f"Terjadi error saat menarik data: {e}")
        break

print("\nProses scraping selesai. Mulai memproses dan melabeli data...")

# Mengubah hasil scraping menjadi format tabel 
df = pd.DataFrame(all_reviews)

# Kita hanya mengambil kolom teks ulasan ('content') dan rating ('score')
df = df[['content', 'score']]

# pelabelan 3 kelas
def assign_label(score):
    if score <= 2:
        return 'Negatif'
    elif score == 3:
        return 'Netral'
    else:
        return 'Positif'

# Menerapkan pelabelan ke kolom baru 'label'
df['label'] = df['score'].apply(assign_label)

# Membersihkan data dengan menghapus baris yang teks ulasannya kosong
df.dropna(subset=['content'], inplace=True)

# Menghapus duplikat data 
df.drop_duplicates(subset=['content'], inplace=True)

# Menyimpan ke file CSV
filename = 'dataset_ruangguru.csv'
df.to_csv(filename, index=False)

print("\n=== RINGKASAN HASIL SCRAPING ===")
print(f"File berhasil disimpan sebagai: {filename}")
print(f"Total data bersih siap pakai : {len(df)} baris")
print("\nDistribusi Kelas Sentimen:")
print(df['label'].value_counts())