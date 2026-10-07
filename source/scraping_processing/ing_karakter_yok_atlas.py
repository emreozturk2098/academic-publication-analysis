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

# Başlıkları çıkarma fonksiyonu
def remove_titles(name):
    titles = [
        "PROFESÖR", "DOÇENT", "ÖĞRETİM GÖREVLİSİ", "ARAŞTIRMA GÖREVLİSİ", "DOKTOR ÖĞRETİM ÜYESİ", "(Unvan:Docent) ","(Kismi Zamanli, Yurt Ici) "
    ]
    for title in titles:
        name = name.replace(title, "").strip()
    return name

# Parantez içindeki tüm ifadeleri kaldırma fonksiyonu
def remove_parentheses(text):
    return re.sub(r'\(.*?\)', '', text).strip()

# Excel dosyalarını işlemek ve verileri birleştirmek
def process_and_combine_excel_files(input_directory, output_csv_file):
    all_author_names = []  # Tüm yazar isimlerini burada tutacağız

    # Giriş dizinindeki tüm alt klasörleri gez
    for root, dirs, files in os.walk(input_directory):
        # Yalnızca "data_from__ÜNİ_TİTLE_HOCA_full" ismiyle başlayan Excel dosyalarını al
        excel_files = [f for f in files if f.startswith('data_from__ÜNİ_TİTLE_HOCA_full') and (f.endswith('.xlsx') or f.endswith('.xls'))]
        
        for file in excel_files:
            input_file = os.path.join(root, file)
            
            # Excel dosyasını oku
            data = pd.read_excel(input_file)

            # "Name and Title" sütununu kontrol et
            if 'Name and Title' in data.columns:
                def clean_and_format_names(names):
                    if pd.isna(names):  # Eğer değer boşsa, boş string döndür
                        return ""
                    names = str(names)  # Veriyi stringe çevir
                    # Başlıkları çıkar
                    names = remove_titles(names)
                    # Parantez içindeki ifadeleri kaldır
                    names = remove_parentheses(names)
                    # Türkçe karakterleri İngilizce karakterlere dönüştür
                    return turkish_to_english_chars(names)

                # İsimleri temizle ve formatla
                author_names = data['Name and Title'].apply(clean_and_format_names)
                
                # Tüm yazar isimlerini birleştir
                all_author_names.extend(author_names)
            else:
                print(f"'{file}' dosyasında 'Name and Title' sütunu bulunamadı.")

    # Birleştirilmiş tüm verileri DataFrame'e dönüştür
    combined_data = pd.DataFrame({'Name and Title': all_author_names})

    # Tüm verileri tek bir CSV dosyasına kaydet
    combined_data.to_csv(output_csv_file, index=False)
    print(f"Tüm veriler başarıyla birleştirildi ve dosya şurada kaydedildi: {output_csv_file}")

# Excel dosyalarını işle ve verileri birleştir
process_and_combine_excel_files(input_directory, output_csv_file)
