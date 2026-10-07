import pandas as pd

# Excel dosyalarının yolları
file1 = './data/inputs/final_scopus_with_genders_1854_2015.xlsx'
file2 = './data/inputs/final_scopus_with_genders_2016_2024.xlsx'

# Verileri yükle
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# DataFrame'leri birleştir
df = pd.concat([df1, df2], ignore_index=True)

# "Unknown" olanları çıkar
filtered_df = df[~df['Gender Predictions'].str.contains('Unknown', na=False)]

# Sonuçları tutacak bir DataFrame oluştur
gender_counts = []

# Her satırı işleyerek cinsiyet ve yıl bazında makale sayılarını hesapla
for _, row in filtered_df.iterrows():
    year = row['Year']
    genders = row['Gender Predictions'].split(';')
    for gender in genders:
        gender_counts.append({'Year': year, 'Gender': gender.strip(), 'Number of Articles': 1})

# DataFrame'e dönüştür ve gruplandırarak sayıları hesapla
results_df = pd.DataFrame(gender_counts)
grouped_results = results_df.groupby(['Year', 'Gender']).sum().reset_index()

# Sonuçları Excel'e kaydet
output_path = './data/inputs/gender_article_counts.xlsx'
grouped_results.to_excel(output_path, index=False)

print(f"Sonuçlar başarıyla kaydedildi: {output_path}")