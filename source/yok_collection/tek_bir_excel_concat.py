import pandas as pd

# Excel dosyasının tam yolunu belirtin
input_file_path = './data/inputs/data_from__ÜNİ_TİTLE_HOCA_full.xlsx'
output_file_path = './data/inputs/güncellenmiş_dosya.xlsx'

# Excel dosyasını okuyun
df = pd.read_excel(input_file_path)

# Metnin her kelimesinin baş harfini büyük yapmak için fonksiyon
def title_case(text):
    if isinstance(text, str):
        # Her kelimenin baş harfini büyük yapar
        return ' '.join([word.capitalize() for word in text.split()])
    return text

# "Department" sütunundaki verilerle yeni sütunları oluştururken, "University Name" sütununu dolduralım
df['University Name'] = df['Department'].apply(lambda x: title_case(x.split('/')[0]) if isinstance(x, str) else '')
df['Faculty'] = df['Department'].apply(lambda x: title_case(x.split('/')[1]) if len(x.split('/')) > 1 else '')
df['Department'] = df['Department'].apply(lambda x: title_case(x.split('/')[2]) if len(x.split('/')) > 2 else '')

# "Name and Title" sütunundaki verileri "Name, Surname and Title" olarak 4. sütuna kopyalayalım
df['Name, Surname and Title'] = df['Name and Title'].apply(lambda x: title_case(x))

# "Department" sütunundaki boş satırları (NaN veya boş değerleri) silmek için
df = df[df['Department'].notna()]  # Department sütunundaki boş (NaN) satırları siler

# Sütun sırasını yeniden düzenleyelim
df = df[['University Name', 'Faculty', 'Department', 'Name, Surname and Title']]

# Sonuçları yeni bir Excel dosyasına kaydedelim
df.to_excel(output_file_path, index=False)

print(f"İşlem tamamlandı. Güncellenmiş dosya: {output_file_path}")
