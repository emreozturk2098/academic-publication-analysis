import os
import pandas as pd

# Klasör yolu ve çıkış Excel dosyası yolu
folder_path = './data/inputs/All_years'
output_excel_path = './data/inputs/final_result.xlsx'

# Birleştirme için boş bir DataFrame oluştur
merged_df = pd.DataFrame()

# Klasördeki tüm dosyaları sırayla işlemek (ters sırayla)
for file_name in reversed(os.listdir(folder_path)):
    # Sadece CSV ve Excel dosyalarını işle
    if file_name.endswith(".csv") or file_name.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file_name)  # Tam yolu oluştur
        
        try:
            # Dosyanın türüne göre okuma işlemi
            if file_name.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file_name.endswith(".xlsx"):
                df = pd.read_excel(file_path)
            
            # Seçilen sütunları ayıkla
            columns_to_extract = ["Author full names", "Document Type", "Title", "Year", "Affiliations"]
            selected_columns_df = df[columns_to_extract]
            
            # Birleştir
            merged_df = pd.concat([merged_df, selected_columns_df], ignore_index=True)
            print(f"İşleniyor: {file_path}")
        
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {file_path}")
        except KeyError as e:
            print(f"Sütun eksikliği nedeniyle hata oluştu: {file_name}, Eksik sütun: {e}")
        except Exception as e:
            print(f"Diğer bir hata oluştu: {file_name}, Hata: {e}")

# Birleştirilen veriyi Excel dosyasına kaydet
merged_df.to_excel(output_excel_path, index=False)

print(f"Bütün dosyalar başarıyla birleştirildi ve kaydedildi: {output_excel_path}")
