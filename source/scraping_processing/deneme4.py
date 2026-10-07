import pandas as pd
import matplotlib.pyplot as plt
import os

# Dosya yolunu belirtin
file_path = './data/inputs/final_match_with_type_cities.xlsx'

# Çıktı klasörünü tanımlayın
output_folder = './data/inputs/Gender'

# Alt klasörler oluşturuluyor
excel_folder = os.path.join(output_folder, 'excel_files')
graph_folder = os.path.join(output_folder, 'graphs')
os.makedirs(excel_folder, exist_ok=True)
os.makedirs(graph_folder, exist_ok=True)

# Veriyi oku
data = pd.read_excel(file_path)

# Geçerli unvanlar listesi
valid_titles = ["Arastirma Gorevlisi", "Docent", "Profesor", "Doktor Ogretim Uyesi"]

# "Title, Name and Surname" sütununda geçerli unvanlara sahip satırları filtrele
filtered_data = data[data['Title, Name and Surname'].str.contains('|'.join(valid_titles), case=False, na=False)]

# Fakülte ve Title bazında toplam sayıyı hesapla
faculty_title_counts = filtered_data.groupby(['Faculty', 'Title, Name and Surname']).size().unstack(fill_value=0)

# Fakülte bazında işlem yapmak için her bir fakülteyi gruplayalım
for faculty in faculty_title_counts.index:
    # Fakülteye ait veriyi al
    faculty_data = faculty_title_counts.loc[faculty]

    # Excel dosyasına kaydet
    excel_filename = f'{faculty}_title_distribution.xlsx'
    faculty_data.to_excel(os.path.join(excel_folder, excel_filename))

    # Grafik oluştur (Yatay Bar)
    plt.figure(figsize=(12, 8))
    faculty_data.plot(kind='barh', colormap='tab20', legend=True)
    plt.title(f'{faculty} Faculty Title Distribution')
    plt.xlabel('Count')
    plt.ylabel('Titles')
    plt.tight_layout()

    # Grafik üzerine değerleri ekleyelim
    for i, value in enumerate(faculty_data):
        plt.text(value + 0.5, i, str(value), va='center', fontsize=10, color='black')

    # Grafik kaydet
    plt.savefig(os.path.join(graph_folder, f'{faculty}_title_distribution.png'))
    plt.close()

    print(f"'{faculty}' Fakültesi için Title Dağılım grafiği '{graph_folder}/{faculty}_title_distribution.png' konumuna kaydedildi.")

# Tüm fakülteler ve unvanların toplamını Excel'e yazdır
faculty_title_summary_path = os.path.join(excel_folder, 'faculty_title_summary.xlsx')
faculty_title_counts.to_excel(faculty_title_summary_path)

print(f"Tüm fakülteler ve unvanların toplamı '{faculty_title_summary_path}' dosyasına kaydedildi.")
