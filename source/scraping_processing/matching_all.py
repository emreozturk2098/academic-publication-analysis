import os
import pandas as pd

# Dosya yolunu ve çıktı dizinini belirtin
file1_path = './data/inputs/universites_full_upper.csv'
file2_path = './data/inputs/scopus_data_fulll_upper.csv'
output_dir = './data/inputs/SCRAP'  # Çıktı dosyasını kaydedeceğiniz klasör

# Eğer çıktı klasörü yoksa oluşturun
os.makedirs(output_dir, exist_ok=True)

# Veriyi yükleyin
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Dosya 1'deki "Name and Title" sütununu ayırarak isim ve soyadı alın
df1['Name'] = df1['Name and Title'].apply(lambda x: x.split(' ', 1)[-1] if isinstance(x, str) else str(x))  # Sadece isim kısmını al
df1['Title'] = df1['Name and Title'].apply(lambda x: x.split(' ', 1)[0] if isinstance(x, str) else str(x))  # Unvan kısmını al

# Dosya 2'deki "Author full names" sütununu ; ile ayırarak her bir ismi alıyoruz
df2['Author full names'] = df2['Author full names'].apply(lambda x: str(x).split(';') if isinstance(x, str) else [str(x)])

# Eşleşme işlemi: Yalnızca 'Author full names' ve 'Name and Title' sütunlarını karşılaştır
matched_data = []

for idx1, row1 in df1.iterrows():
    name1 = str(row1['Name'])  # İsim kısmını alıyoruz
    title1 = str(row1['Title'])  # Unvan kısmını alıyoruz
    name_and_title1 = str(row1['Name and Title'])  # Tam 'Name and Title'

    for idx2, row2 in df2.iterrows():
        # Dosya 2'deki isimleri kontrol et
        for author_name in row2['Author full names']:
            author_name = str(author_name)  # Yine string'e çeviriyoruz
            # Eğer dosya 2'deki isimle eşleşme varsa
            if name_and_title1 == author_name:  # Tam eşleşme sağlanıyor
                # Eşleşen ismi ve unvan bilgisini ekle
                matched_data.append({
                    'Name and Title': name_and_title1,
                    'Author full names': author_name
                })

# Elde edilen eşleşmeleri yeni bir DataFrame'e dönüştürün
matched_df = pd.DataFrame(matched_data)

# Çıktı dosyasını kaydedin
output_file = os.path.join(output_dir, 'matched_data_full.csv')
matched_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Eşleşmiş veriler başarıyla {output_file} olarak kaydedildi.")
