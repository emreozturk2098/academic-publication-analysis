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
time.sleep(2)  # Sayfanın yüklenmesi için bekleyin
 
# İkinci URL'ye geçiş yapmak için düğmeye tıklama
try:
    second_url_xpath = '/html/body/div/div[2]/div/table/tbody/tr[17]/td[1]/a'  # Düğme XPath
    button = driver.find_element(By.XPATH, second_url_xpath)
    button.click()
    time.sleep(2)  # Yeni sayfanın yüklenmesini bekleyin
except Exception as e:
    print(f"Error clicking the button to navigate: {e}")
    driver.quit()
    exit()
 
# Tüm sayfalardan sonuçları toplamak için liste
all_data = []
 
try:
    # Sayfa yüklenmeden önce 3 kez "Sonraki" düğmesine bas
    for _ in range(0):  # 3 kez "Sonraki" düğmesine bas
        try:
            next_group_xpath = '/html/body/div/div[2]/div[2]/div[2]/ul/li[12]/a'  # "Sonraki" düğmesi XPath
            next_group_button = driver.find_element(By.XPATH, next_group_xpath)
            next_group_button.click()
            time.sleep(0.5)  # Yeni sayfanın yüklenmesini bekle
        except Exception as next_group_error:
            print(f"Error clicking 'Sonraki' button: {next_group_error}")
            break
 
    # 12 döngü boyunca sayfalama işlemi yap
    for _ in range(15):  # Bu döngü 12 kez tekrar edecek
        print(f"Processing page group...")
 
        # Sayfa 3'ten 11'e kadar olan sayfaları gez
        for page in range(3, 13):  # 3'ten 11'e kadar olan sayfalar
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
                        department_text = row.find_element(By.XPATH, department_xpath).text.strip()
                        department = f"{department_text}"
                    except:
                        department = ''  # Bölüm yoksa boş bırak
 
                    # Veriyi listeye ekle
                    all_data.append([f"{title} {name}", department])
 
                except Exception as row_error:
                    print(f"Error processing row: {row_error}")
 
            # Sayfayı ilerlet
            if page < 12:  # Eğer son sayfa değilse
                try:
                    next_page_xpath = f'/html/body/div/div[2]/div[2]/div[2]/ul/li[{page}]/a'
                    next_button = driver.find_element(By.XPATH, next_page_xpath)
                    next_button.click()
                    time.sleep(2)  # Sayfanın yüklenmesi için bekle
                except Exception as next_error:
                    print(f"Error navigating to page {page}: {next_error}")
                    break
 
        # "Sonraki" düğmesine bas
        try:
            next_group_xpath = '/html/body/div/div[2]/div[2]/div[2]/ul/li[12]/a'  # "Sonraki" düğmesi XPath
            next_group_button = driver.find_element(By.XPATH, next_group_xpath)
            next_group_button.click()
            time.sleep(3)  # Yeni sayfanın yüklenmesini bekle
        except Exception as next_group_error:
            print(f"Error clicking 'Sonraki' button: {next_group_error}")
            break
 
except Exception as e:
    print(f"Error occurred during scraping: {e}")
 
# Veriyi DataFrame'e çevirme
df = pd.DataFrame(all_data, columns=["Name and Title", "Department"])
 
# Excel dosyasına kaydetme
file_path = r"C:\Users\emre.ozturk\Desktop\Üni_title_hocalar2.xlsx"
df.to_excel(file_path, index=False, header=True)
 
print(f"All data has been saved to {file_path}")
 
# Tarayıcıyı kapat
driver.quit()