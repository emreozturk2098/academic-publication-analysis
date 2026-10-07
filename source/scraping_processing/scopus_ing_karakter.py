import pandas as pd
import re

# Giriş ve çıkış dosyalarının yolları
input_file = './data/inputs/csv_result_all.csv'
output_file = './data/inputs/csv_buyuk_harf.csv'

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

# İngilizce büyük harfe dönüştürme fonksiyonu
def english_upper(text):
    return turkish_to_english_chars(text).upper()

# CSV dosyasını oku
data = pd.read_csv(input_file)

# 'Author full names' sütununu seç ve düzenlemeleri yap
if 'Author full names' in data.columns:
    def clean_and_format_names(names):
        if pd.isna(names):  # Eğer değer boşsa, boş string döndür
            return ""
        names = str(names)  # Veriyi stringe çevir
        # Parantez içindeki ifadeleri kaldır
        names = re.sub(r"\(.*?\)", "", names).strip()
        # ; ile ayrılmış tüm isimleri ayır ve tek tek işle
        processed_names = []
        for name in names.split(";"):
            name = name.strip()
            # Soyisim, İsim -> İsim, Soyisim olarak çevir
            parts = name.split(",")
            if len(parts) == 2:
                surname = parts[0].strip()
                given_names = parts[1].strip()
                formatted_name = f"{given_names} {surname}".strip()
            else:
                formatted_name = name.strip()  # Eğer virgül yoksa olduğu gibi döndür
            
            # Büyük harfe çevir
            corrected_name = english_upper(formatted_name)
            processed_names.append(corrected_name)
        # İşlenmiş isimleri tekrar ; ile birleştir
        return "; ".join(processed_names)

    # İsimleri temizle ve formatla
    author_names = data['Author full names'].apply(clean_and_format_names)
    
    # Yeni DataFrame'e dönüştür
    output_data = pd.DataFrame({'Author full names': author_names})
    # Yeni CSV dosyasını kaydet
    output_data.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"İşlem başarıyla tamamlandı ve dosya şurada kaydedildi: {output_file}")
else:
    print("'Author full names' sütunu dosyada bulunamadı. Lütfen doğru dosyayı seçtiğinizden emin olun.")
