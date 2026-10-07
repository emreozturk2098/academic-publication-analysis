import pandas as pd
import gender_guesser.detector as gender

# Excel dosyasını oku
df = pd.read_excel('./data/inputs/final_scopus_with_type_2016_2024_cleaned.xlsx')

# Gender-Guesser dedektörü
d = gender.Detector()

def predict_gender(name):
    """Tek bir isim için cinsiyet tahmini yapar."""
    first_name = name.split()[0]  # İlk ismi al
    gender_guess = d.get_gender(first_name)
    if gender_guess in ['male', 'mostly_male']:
        return 'Male'
    elif gender_guess in ['female', 'mostly_female']:
        return 'Female'
    else:
        return 'Unknown'

def process_authors(authors):
    """Birden fazla isim için cinsiyet tahmini yapar."""
    if isinstance(authors, str):  # Eğer metin ise işleme devam et
        author_list = authors.split(';')  # İsimleri ayır
        genders = [predict_gender(author.strip()) for author in author_list]
        return '; '.join(genders)  # Tahminleri ; ile birleştir
    return 'Unknown'  # Metin değilse Unknown döndür

# Yeni sütun oluştur ve cinsiyet tahminlerini ekle
df['Gender Predictions'] = df['Author full names'].apply(process_authors)

# Yeni Excel dosyasına kaydet
output_path = './data/inputs/final_scopus_with_genders_2016_2024.xlsx'
df.to_excel(output_path, index=False)

print(f"Cinsiyet tahminleri tamamlandı. Çıktı: {output_path}")