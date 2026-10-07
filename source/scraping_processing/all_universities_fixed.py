import pandas as pd

# Dosya yolu
file_path = './data/inputs/updated_gender_data_with_finalllllllllll.xlsx'

# Veriyi yükle
df = pd.read_excel(file_path)

# Yeni isim listesi
names_to_update = [
    "Afig", "Afksendiyos", "Agop", "Ahadollah", "Ahmi", "Ahsanollah", "Akansel", 
    "Akcan", "Akkin", "Alaskar", "Alauddin", "Alkin", "Allaberen", "Alphan", 
    "Alpturk", "Amac", "Aminu", "And", "Anday", "Aptullah", "Araks", "Arbil", "Arcan"
]

# Gender sütununda 'unknown' olan satırları filtrele ve 'Academic Name' ile eşleşen isimler için 'Gender' değerini 'Male' yap
df.loc[(df['Gender'] == 'unknown') & (df['Academic Name'].str.split().str[0].isin(names_to_update)), 'Gender'] = 'Male'

# Sonuçları yeni bir dosyaya kaydet
output_path = './data/inputs/updated_gender_data_with_finalllllllllll.xlsx'
df.to_excel(output_path, index=False)

# Kaydedilen dosyanın yolunu yazdır
print(f"Veri güncellendi ve kaydedildi: {output_path}")
