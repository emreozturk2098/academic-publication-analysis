import os
import pandas as pd
from glob import glob

# Türkçe karakterleri İngilizce karakterlere dönüştürmek için bir fonksiyon
def convert_to_english_characters(text):
    conversion_table = {
        'ç': 'c', 'Ç': 'C', 'ş': 's', 'Ş': 'S', 'ı': 'i', 'I': 'i', 
        'ğ': 'g', 'Ğ': 'G', 'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 
        'ı': 'i', 'İ': 'i'
    }
    for key, value in conversion_table.items():
        text = text.replace(key, value)
    return text

# Kaynak ve çıktı dizinlerini belirtin
source_dir = './data/inputs/All'
output_dir = './data/inputs/SCRAP'

# Alt klasörlerdeki tüm excel dosyalarını bulun
file_pattern = os.path.join(source_dir, '**', 'data_from__ÜNİ_TİTLE_HOCA_full.xlsx')
files = glob(file_pattern, recursive=True)

# Excel dosyalarını birleştirme
dfs = []
for file in files:
    df = pd.read_excel(file)

    # Her hücredeki Türkçe karakterleri İngilizce karakterlere dönüştürme ve büyük harfe çevirme
    for col in df.columns:
        df[col] = df[col].apply(lambda x: convert_to_english_characters(str(x)).upper() if isinstance(x, str) else x)
    
    dfs.append(df)

# Tüm verileri birleştir
combined_df = pd.concat(dfs, ignore_index=True)

# Birleştirilmiş veriyi yeni bir dosyaya CSV olarak kaydet
output_file = os.path.join(output_dir, 'universites_full.csv')
combined_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Birleştirilmiş dosya {output_file} olarak kaydedildi.")
