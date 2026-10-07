import pandas as pd

# Dosya yolu
file_path = './data/inputs/updated_gender_data_with_finalllllllllll.xlsx'

# Veriyi yükle
df = pd.read_excel(file_path)

# Gender sütununda "unknown" olan satırları filtrele
unknown_gender_df = df[df['Gender'] == 'unknown']

# "Academic Name" sütunundaki isimlerden sadece ilk kelimeyi al
unknown_gender_df['First Name'] = unknown_gender_df['Academic Name'].str.split().str[0]

# İlk kelimelerin tekrar sayısını bul
first_name_counts = unknown_gender_df['First Name'].value_counts()

# Sonuçları DataFrame'e dönüştür
first_name_counts_df = first_name_counts.reset_index()
first_name_counts_df.columns = ['First Name', 'Count']  # Kolon adlarını yeniden adlandır

# Excel dosyasına kaydet
output_path = './data/inputs/first_name_counts_for_unknown_gender.xlsx'
first_name_counts_df.to_excel(output_path, index=False)

# Sonuçları yazdır
print(first_name_counts_df)
