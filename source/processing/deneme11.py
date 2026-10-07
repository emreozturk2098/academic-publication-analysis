import pandas as pd
import difflib

# Dosyaları yükle
file_path_1 = './data/inputs/final_scopus_fixed.xlsx'
file_path_2 = './data/inputs/organized_all_Türkiye_universities_academics_copy.xlsx'

df1 = pd.read_excel(file_path_1)
df2 = pd.read_excel(file_path_2)

# 1. Dosyadaki 'Author full names' sütunundaki isimleri ayırma
df1['Author full names'] = df1['Author full names'].str.split(';')

# Fonksiyon: en yakın eşleşmeyi bulma
def get_best_match(name, names_list):
    match = difflib.get_close_matches(name, names_list, n=1, cutoff=0.8)  # %80 benzerlik arıyoruz
    return match[0] if match else None

# 2. Dosyadaki 'Academic Name' sütunundaki tüm isimleri liste olarak al
academic_names = df2['Academic Name'].tolist()

# Yeni bir sütun ekleyerek, 'Author full names' ile 'Academic Name' eşleştirmesi yapıyoruz
df1['Matched Academic Name'] = df1['Author full names'].apply(lambda authors: [
    get_best_match(author.strip(), academic_names) for author in authors
])

# 3. Eşleşen akademik isimlere göre diğer bilgileri eşleştiriyoruz
# Burada df2 ile df1'i 'Matched Academic Name' üzerinden birleştiriyoruz
df1['Matched Academic Name'] = df1['Matched Academic Name'].apply(lambda x: x[0] if isinstance(x, list) else None)  # İlk eşleşmeyi al

# Merge işlemi: df1 ve df2'yi Matched Academic Name'e göre birleştiriyoruz
merged_df = pd.merge(df1, df2, left_on='Matched Academic Name', right_on='Academic Name', how='left')

# Sonuçları kaydet
merged_df.to_excel('./data/inputs/merged_output.xlsx', index=False)

# Sonuçları görüntüleyelim
print(merged_df.head())
