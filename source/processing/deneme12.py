import pandas as pd
import os

# Girdi ve çıktı dizinlerini belirtin
input_dir = './data/inputs/All_years'
output_file = './data/inputs/combined_data.xlsx'

# Excel dosyalarını almak için dizini kontrol et
excel_files = [f for f in os.listdir(input_dir) if f.endswith('.xlsx')]

# Boş bir liste oluşturun, tüm verileri bu listede birleştireceğiz
all_data = []

# Her Excel dosyasını oku ve verilerini listeye ekle
for file in excel_files:
    file_path = os.path.join(input_dir, file)
    df = pd.read_excel(file_path)
    all_data.append(df)

# Tüm verileri birleştir
combined_data = pd.concat(all_data, ignore_index=True)

# Birleştirilen veriyi yeni bir Excel dosyasına kaydet
combined_data.to_excel(output_file, index=False)

print(f"Veriler başarıyla {output_file} olarak kaydedildi.")
