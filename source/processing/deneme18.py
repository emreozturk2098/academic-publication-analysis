import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Dosya yolları
file1 = './data/inputs/final_scopus_with_genders_1854_2015.xlsx'
file2 = './data/inputs/final_scopus_with_genders_2016_2024.xlsx'

# Verileri yükle
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Dosyaları birleştir
df = pd.concat([df1, df2], ignore_index=True)

# Şehirleri ve yıl bazında makale sayısını hesaplamak
df['City'] = df['City'].fillna('')  # NaN değerlerini boş string ile doldur
df['City'] = df['City'].apply(lambda x: x.split(';') if x else [])  # Şehirleri ayır

# Her bir şehir için ayrı satırlar oluştur
expanded_df = df.explode('City')

# Her şehir için tüm yıllarda toplam makale sayısını hesapla
city_total_count = expanded_df.groupby('City').size().reset_index(name='Total Article Count')

# Grafik klasörünü oluştur
output_folder = './data/inputs/results'
os.makedirs(output_folder, exist_ok=True)

# Excel dosyası için çıktı yolu
excel_output_path = './data/inputs/city_total_article_counts.xlsx'

# Excel'e kaydetme işlemi
city_total_count.to_excel(excel_output_path, index=False)

# Şehirlerin toplam makale sayısını görselleştirme
plt.figure(figsize=(12, 8))
sns.barplot(data=city_total_count, x='City', y='Total Article Count', color='skyblue')
plt.xticks(rotation=90, ha='right', fontsize=10)
plt.xlabel('City')
plt.ylabel('Total Number of Articles')
plt.title('Total Number of Articles by City')

# Grafik kaydet
city_output_path = os.path.join(output_folder, 'total_city_article_counts.png')
plt.tight_layout()
plt.savefig(city_output_path)
plt.close()
