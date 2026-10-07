import pandas as pd

# Dosya yolları
file1 = './data/inputs/all_universites_ing_karakter.csv'
file2 = './data/inputs/csv_buyuk_harf.csv'
output_file = './data/inputs/final_matched.csv'  # Eşleşen verilerin kaydedileceği dosya

# Dosyaları oku
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# 'Author full names' sütununu kullanarak eşleşen verileri bulmak
# df2'de birden fazla sütunda isimler olduğunu varsayıyoruz (örneğin 'Name1', 'Name2', 'Name3' gibi)

# Eşleşen verileri saklamak için bir liste
matched_data = []

# Her bir df2 sütununda 'Author full names' ile eşleşen isimleri bul
for column in df2.columns:
    # 'Author full names' ile her bir sütundaki isimleri karşılaştır
    matched = pd.merge(df1, df2[[column]], left_on='Author full names', right_on=column, how='inner')
    matched_data.append(matched)

# Tüm eşleşen verileri birleştir
final_matched_data = pd.concat(matched_data)

# Eşleşen verileri CSV dosyasına kaydet
final_matched_data.to_csv(output_file, index=False)

print(f"Eşleşen veriler başarıyla kaydedildi: {output_file}")
