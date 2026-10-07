import pandas as pd
import re
import os

# Giriş dosyasının bulunduğu dizin ve çıktı dosyasının yolu
input_directory = './data/inputs/All'  # Dosyaların bulunduğu dizin
output_directory = './data/inputs/Scopus'  # Çıktı dosyalarının kaydedileceği dizin
output_csv_file = os.path.join(output_directory, "all_universites_ing_karakter_full.csv")  # Birleştirilmiş CSV dosyasının yolu

# Türkçe karakterleri İngilizce karakterlere dönüştürme fonksiyonu
def turkish_to_english_chars(text):
    turkish_to_english = {
        "Ç": "C",
        "Ğ": "G",
        "İ": "I",
        "Ö": "O",
        "Ş": "S",
        "Ü": "U",
        "ı": "i",
        "ç": "c",
        "ğ": "g",
        "ö": "o",
        "ş": "s",
        "ü": "u"
    }
    return ''.join(turkish_to_english.get(char, char) for char in text)

# Parantez içindeki tüm ifadeleri kaldırma fonksiyonu
def remove_parentheses(text):
    return re.sub(r'\(.*?\)', '', text).strip()

# Temizleme işlemini tüm sütunlar için uygulama fonksiyonu
def clean_and_format_text(text):
    if pd.isna(text):  # Eğer değer boşsa, boş string döndür
        return ""
    text = str(text)  # Veriyi stringe çevir
    # Parantez içindeki ifadeleri kaldır
    text = remove_parentheses(text)
    # Türkçe karakterleri İngilizce karakterlere dönüştür
    text = turkish_to_english_chars(text)
    # Her kelimenin baş harfini büyüt
    return text.title()

# Excel dosyalarını işlemek ve verileri birleştirmek
def process_and_combine_excel_files(input_directory, output_csv_file):
    all_dataframes = []  # Tüm işlenmiş DataFrame'leri burada tutacağız

    # Giriş dizinindeki tüm alt klasörleri gez
    for root, dirs, files in os.walk(input_directory):
        # Yalnızca "data_from__ÜNİ_TİTLE_HOCA_full" ismiyle başlayan Excel dosyalarını al
        excel_files = [f for f in files if f.startswith('data_from__ÜNİ_TİTLE_HOCA_full') and (f.endswith('.xlsx') or f.endswith('.xls'))]
        
        for file in excel_files:
            input_file = os.path.join(root, file)
            
            # Excel dosyasını oku
            data = pd.read_excel(input_file)

            # Tüm sütunlar üzerinde temizleme işlemini uygula
            for column in data.columns:
                data[column] = data[column].apply(clean_and_format_text)

            # Temizlenmiş DataFrame'i listeye ekle
            all_dataframes.append(data)

    # Tüm işlenmiş DataFrame'leri birleştir
    combined_data = pd.concat(all_dataframes, ignore_index=True)

    # Birleştirilmiş tüm verileri CSV dosyasına kaydet
    combined_data.to_csv(output_csv_file, index=False)
    print(f"Tüm veriler başarıyla birleştirildi ve dosya şurada kaydedildi: {output_csv_file}")

# Excel dosyalarını işle ve verileri birleştir
process_and_combine_excel_files(input_directory, output_csv_file)
