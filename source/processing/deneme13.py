import pandas as pd
from unidecode import unidecode
import re
 
# Dosya yolu ve yeni dosya adı
input_file = './data/inputs/combined_data.xlsx'
output_file = './data/inputs/combined_data_processed.xlsx'
 
# Excel dosyasını yükle
df = pd.read_excel(input_file)
 
# Tüm sütunlardaki yazıları İngilizce karakterlere çevir
df = df.applymap(lambda x: unidecode(str(x)) if isinstance(x, str) else x)
 
# Author full names sütununu işlemek için fonksiyonlar
def clean_author_names(authors):
    if not isinstance(authors, str):
        return authors
 
    # Parantez içindeki sayıları ve parantezleri temizle
    authors = re.sub(r"\([^)]*\)", "", authors).strip()
 
    # Noktalı virgül ile ayrılmış isimleri işlemek
    author_list = authors.split(";")
    cleaned_authors = []
 
    for author in author_list:
        name_parts = author.split(",")
        if len(name_parts) == 2:
            last_name, first_name = name_parts
            cleaned_authors.append(first_name.strip() + " " + last_name.strip())
 
    return "; ".join(cleaned_authors)
 
# Author full names sütununu işleme tabi tut
df['Author full names'] = df['Author full names'].apply(clean_author_names)
 
# Affiliations sütununu işlemek için fonksiyon
def extract_university_info(affiliations):
    if not isinstance(affiliations, str):
        return affiliations
 
    # Sadece University geçen bilgileri ayıkla
    university_list = [info.strip() for info in affiliations.split(";") if "University" in info]
    return "; ".join(university_list)
 
# Affiliations sütununu işleme tabi tut
df['Affiliations'] = df['Affiliations'].apply(extract_university_info)
 
# Yeni City sütununu eklemek için fonksiyon
def extract_city_info(affiliations):
    cities = [
        "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kirikkale", "Kirklareli", "Kirsehir", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa", "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Sanliurfa", "Sirnak", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"
    ]
    if not isinstance(affiliations, str):
        return None
 
    found_cities = [city for city in cities if city in affiliations]
    return "; ".join(found_cities) if found_cities else None
 
# City sütununu ekle
df['City'] = df['Affiliations'].apply(extract_city_info)
 
# İşlenmiş veriyi yeni bir Excel dosyasına kaydet
df.to_excel(output_file, index=False)
 
print(f"İşlenmiş dosya başarıyla kaydedildi: {output_file}")