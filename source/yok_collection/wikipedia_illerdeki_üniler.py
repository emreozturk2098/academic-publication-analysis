from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Chrome seçeneklerini ayarlayın
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./work/browser_profile')
options.add_argument("--profile-directory=Profile 2")

# Chrome WebDriver başlatma
driver = webdriver.Chrome(options=options)

# Wikipedia URL'si
url = './data/inputs/Kategori:Kayseri_ilindeki_%C3%BCniversiteler'

# Excel'e kaydedilecek veriler
data = []

# URL'yi açalım
driver.get(url)
time.sleep(2)  # Sayfanın yüklenmesi için bekleyin

try:
    # Belirtilen XPath'teki tüm elemanları çek
    elements = driver.find_elements(By.XPATH, '//*[@id="mw-pages"]/div')

    # Her elemandan metni al ve listeye ekle
    for element in elements:
        text = element.text.strip()
        if text:  # Boş olmayan metinleri ekle
            data.append(text)  # Sadece metni ekle

    print(f"Data collected from {url}")

except Exception as e:
    print(f"Error extracting data from {url}: {e}")

# Veriyi DataFrame'e çevirme (her satır bir üniversite adı olarak sütun altına gelir)
df = pd.DataFrame(data, columns=["Üniversitenin Adı"])

# Excel dosyasına kaydetme
file_path = './data/inputs/universities_in_Kayseri.xlsx'
df.to_excel(file_path, index=False)

# Tarayıcıyı kapat
driver.quit()

print(f"Data has been saved to {file_path}")
