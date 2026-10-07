import pandas as pd
 
# Dosya yolları
file1_path = './data/inputs/final_scopus_fixed.xlsx'
file2_path = './data/inputs/organized_all_Türkiye_universities_academics_copy.xlsx'
output_file = './data/inputs/matched_data.xlsx'
 
# Excel dosyalarını oku
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
 
# 'Author full names' ve 'Academic Name' sütunlarındaki verileri ayır
df1['Author full names'] = df1['Author full names'].str.split(';')
df2['Academic Name'] = df2['Academic Name'].str.split(';')
 
# DataFrame'leri eşleştirmek için, her iki veri setinde de her bir öğeyi karşılaştıracak şekilde genişletiyoruz
df1_expanded = df1.explode('Author full names')
df2_expanded = df2.explode('Academic Name')
 
# Sadece 'Author full names' ve 'Academic Name' sütunları ile eşleşme yap
merged_df = pd.merge(df1_expanded, df2_expanded, left_on='Author full names', right_on='Academic Name')
 
# 'Number of Articles' sütunu için yazar başına makale sayısını hesapla
article_count = merged_df.groupby('Author full names').size().reset_index(name='Number of Articles')
 
# 'Year' sütunu için yazar başına yılları virgülle ayırarak listele (yıl verilerini string'e çevirerek)
years_list = merged_df.groupby('Author full names')['Year'].apply(lambda x: ','.join(map(str, x.unique()))).reset_index(name='Years')
 
# Sonuçları birleştir
merged_df = pd.merge(merged_df, article_count, on='Author full names', how='left')
merged_df = pd.merge(merged_df, years_list, on='Author full names', how='left')
 
# Sonuçları yeni bir Excel dosyasına kaydet
merged_df.to_excel(output_file, index=False)
 
print(f"Eşleşen veriler başarıyla {output_file} olarak kaydedildi.")