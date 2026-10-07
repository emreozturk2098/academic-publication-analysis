import os
import pandas as pd

# Klasör yolunu belirtin
folder_path = './data/inputs/2024'  # Buraya klasör yolunu yazın

# Toplam satır sayısını tutacak değişken
total_rows = 0

# Klasördeki tüm Excel dosyalarını kontrol et
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx") or file_name.endswith(".xls"):  # Sadece Excel dosyalarını kontrol et
        file_path = os.path.join(folder_path, file_name)
        
        try:
            # Excel dosyasını oku
            df = pd.read_excel(file_path)
            
            # Satır sayısını ekle
            total_rows += len(df)
            print(f"{file_name}: {len(df)} satır")
        
        except Exception as e:
            print(f"{file_name} okunamadı: {e}")

# Toplam satır sayısını ekrana bastır
print(f"Klasördeki tüm Excel dosyalarının toplam satır sayısı: {total_rows}")
