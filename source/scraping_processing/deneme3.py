import pandas as pd
from collections import Counter

# Dosya yolu
file_path = './data/inputs/UPDATED_final_match 3.xlsx'

# Excel dosyasını okuma
df = pd.read_excel(file_path)

# Unknown olanları filtreleme
unknown_gender = df[df["Gender"] == "Unknown"]

# "Matched Author Name" sütunundaki isimleri al
names = unknown_gender["Matched Author Name"].dropna()

# İsimlerin sıklığını hesaplama
name_counts = Counter(names)

# Tüm isimlerin sıklığını büyükten küçüğe sıralama
sorted_name_counts = name_counts.most_common()

# Sonuçları ekrana yazdırma
for name, count in sorted_name_counts:
    print(f"İsim: {name}, Sayısı: {count}")
