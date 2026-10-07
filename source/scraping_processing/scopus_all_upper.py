import os
import pandas as pd
import re  # Düzenli ifadeler için

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

# Parantez içindeki rakamları kaldıran fonksiyon
def remove_numbers_in_parentheses(text):
    # Sadece string değerlerle işlem yapılacak
    if isinstance(text, str):
        return re.sub(r'\(\d+\)', '', text)  # \(\d+\) -> parantez içindeki rakamlar
    return text  # Eğer float veya başka bir türse olduğu gibi döndür

# Dosya yolunu ve çıktı dizinini belirtin
file_path = './data/inputs/csv_result_all.csv'
output_dir = './data/inputs/Scopus'  # Çıktı dosyasını kaydedeceğiniz klasör

# Eğer çıktı klasörü yoksa oluşturun
os.makedirs(output_dir, exist_ok=True)

# Veriyi yükleyin
df = pd.read_csv(file_path)

# İlk sütundaki "Author full names" sütununda parantez içindeki rakamları kaldırma
if 'Author full names' in df.columns:
    df['Author full names'] = df['Author full names'].apply(remove_numbers_in_parentheses)

# Her hücredeki Türkçe karakterleri İngilizce karakterlere dönüştürme ve büyük harfe çevirme
for col in df.columns:
    df[col] = df[col].apply(lambda x: convert_to_english_characters(str(x)).upper() if isinstance(x, str) else x)

# Çıktı dosya yolunu oluşturun
output_file = os.path.join(output_dir, 'scopus_data_fulll_upper.csv')

# Sonuçları kaydetme
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Veri başarıyla {output_file} olarak kaydedildi.")
