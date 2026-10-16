from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
 
# Chrome seçeneklerini ayarlayın
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\emre.ozturk\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument("--profile-directory=Profile 2")
 
# Chrome WebDriver başlatma
driver = webdriver.Chrome(options=options)
 
# Başlangıç URL'si
url = "https://akademik.yok.gov.tr/AkademikArama/view/universityListview.jsp"
 
# URL'yi açalım
driver.get(url)
time.sleep(0.5)  # Sayfanın yüklenmesi için bekleyin
 
# İkinci URL'ye geçiş yapmak için düğmeye tıklama
try:
    second_url_xpath = '/html/body/div/div[2]/div/table/tbody/tr[17]/td[1]/a'  # Düğme XPath
    button = driver.find_element(By.XPATH, second_url_xpath)
    button.click()
    time.sleep(0.5)  # Yeni sayfanın yüklenmesini bekleyin
except Exception as e:
    print(f"Error clicking the button to navigate: {e}")
    driver.quit()
    exit()
 
# Tüm sayfalardan sonuçları toplamak için liste
all_data = []
 
try:
    # 1'den 10'a kadar olan sayfaları gez
    for page in range(1, 11):  # 1'den 10'a kadar olan sayfalar
        print(f"Processing page {page}...")
 
        # Sayfadaki tüm yazarların bilgilerini bul
        rows = driver.find_elements(By.XPATH, '//tr[starts-with(@id, "authorInfo_")]')
 
        for row in rows:
            try:
                # Unvan XPath
                title_xpath = './/td[3]/h6[1]'
                title = row.find_element(By.XPATH, title_xpath).text.strip()
 
                # İsim XPath
                name_xpath = './/td[3]/h4/a'
                name = row.find_element(By.XPATH, name_xpath).text.strip()
 
                # Bölüm XPath
                department_xpath = './/td[3]/h6[2]'
                try:
                    department = row.find_element(By.XPATH, department_xpath).text.strip()
                except:
                    department = "Bölüm bilgisi yok"
 
                # Veriyi listeye ekle (Unvan ve isim birleştirilmiş, bölüm ayrı)
                all_data.append([f"{title} {name}", department])
 
            except Exception as row_error:
                print(f"Error processing row: {row_error}")
 
        # Sayfayı ilerlet
        if page < 10:  # Eğer son sayfa değilse
            try:
                next_page_xpath = f'/html/body/div/div[2]/div[2]/div[2]/ul/li[{page + 1}]/a'
                next_button = driver.find_element(By.XPATH, next_page_xpath)
                next_button.click()
                time.sleep(0.5)  # Sayfanın yüklenmesi için bekle
            except Exception as next_error:
                print(f"Error navigating to page {page + 1}: {next_error}")
                break
 
except Exception as e:
    print(f"Error occurred during scraping: {e}")
 
# Veriyi DataFrame'e çevirme
df = pd.DataFrame(all_data, columns=["Name and Title", "Department"])
 
# Excel dosyasına kaydetme
file_path = r"C:\Users\emre.ozturk\Desktop\Üni_title_hocalar.xlsx"
df.to_excel(file_path, index=False, header=True)
 
print(f"All data has been saved to {file_path}")
 
# Tarayıcıyı kapat
driver.quit()