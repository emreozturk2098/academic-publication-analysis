import pandas as pd
import os

# Dosya yolları
file1_path = './data/inputs/matched_data.xlsx'
file2_path = './data/inputs/All_Türkiye_matched_data_with_gender_city_and_type_final 1.xlsx'
output_folder = './data/inputs/Yeni_analiz_scrap'

# Excel dosyalarını yükle
file1_df = pd.read_excel(file1_path)
file2_df = pd.read_excel(file2_path)

# "Academic Name" sütunlarına göre eşleştirme
equal_names = file1_df.merge(file2_df[['Academic Name', 'Gender']], on='Academic Name', how='left')

# Yeni "Gender" sütununu file1_df'ye ekle
file1_df['Gender'] = equal_names['Gender']

# Output klasörü oluştur (eğer yoksa)
os.makedirs(output_folder, exist_ok=True)

# Sonuç dosyasını kaydetme
output_file_path = os.path.join(output_folder, "matched_data_with_gender.xlsx")
file1_df.to_excel(output_file_path, index=False)

print(f"İşlem tamamlandı! Sonuç dosyası: {output_file_path}")
