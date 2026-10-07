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

# Başlangıç URL'si
url = './data/inputs/universityListview.jsp'
driver.get(url)
time.sleep(0.1)  # Sayfanın yüklenmesi için bekleyin

# İkinci URL'ye geçiş yapmak için düğmeye tıklama
try:
    second_url_xpath = '/html/body/div/div[2]/div/table/tbody/tr[179]/td[1]/a'  # Düğme XPath
    button = driver.find_element(By.XPATH, second_url_xpath)
    button.click()
    time.sleep(0.1)  # Yeni sayfanın yüklenmesini bekleyin
except Exception as e:
    print(f"Error clicking the button to navigate: {e}")
    driver.quit()
    exit()

# Tüm sayfalardan sonuçları toplamak için liste
all_data = []

# Sayfa gezintisi (toplam 22 sayfa)
def get_page_xpath(page_number):
    if page_number <= 10:
        return f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{page_number}]/a"
    elif (page_number - 1) % 10 == 0:  # 10, 20 gibi "Next Page" düğmesi
        if page_number == 11:
            return "/html/body/div/div[2]/div[2]/div[2]/ul/li[11]/a"  # 10'dan 11'e geçiş
        else:
            return "/html/body/div/div[2]/div[2]/div[2]/ul/li[12]/a"  # 20'den 21 geçiş
    else:
        inner_page_number = (page_number - 1) % 10 + 2
        return f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{inner_page_number}]/a"

# Sayfa gezintisi (22 sayfa)
try:
    for page in range(1, 131):  # 1'den 22'ye kadar olan sayfalar
        print(f"Processing page {page}...")
        
        # Sayfanın tamamen yüklendiğinden emin olmak için bekleyin
        time.sleep(0.1)  # Bekleme süresini artırdık

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
        if page < 130:  # 22. sayfada yönlendirme yapılmaz
            try:
                next_page_xpath = get_page_xpath(page + 1)
                next_page_button = driver.find_element(By.XPATH, next_page_xpath)
                next_page_button.click()
                time.sleep(0.1)  # Sayfanın yüklenmesi için bekleyin
            except Exception as e:
                print(f"Error navigating to next page: {e}")
                break  # Eğer geçişte hata alırsak, döngüyü sonlandır

except Exception as e:
    print(f"Error processing pages: {e}")

# Veriyi DataFrame'e çevirme
df = pd.DataFrame(all_data, columns=["Name and Title", "Department"])

# Excel dosyasına kaydetme
file_path = './data/inputs/data_from__ÜNİ_TİTLE_HOCA_full.xlsx'
df.to_excel(file_path, index=False, header=True)

print(f"Data has been saved to {file_path}")

# Tarayıcıyı kapat
driver.quit()
