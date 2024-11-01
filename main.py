from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
from time import sleep

workbook = openpyxl.Workbook()
sheet = workbook.active

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--log-level=3")
option.add_argument("--dns-prefetch-disable")
option.add_argument('--no-sandbox')
option.add_argument('--mute-audio')
option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.set_window_size(1280, 720)
link_input = input("Введите ссылку на Каспи категорию")
driver.get(link_input)

# FOR EXAMPLE
# 'https://kaspi.kz/shop/nur-sultan/c/home%20equipment/?q=%3Acategory%3AHome%20equipment%3Aprice%3A10%20000%20-%2049%20999%20%D1%82&sort=relevance&sc='
#

sleep(5)
numberlink = 0
while True:
    try:
        links = driver.find_elements(By.CLASS_NAME, "item-card__name-link")
        for link in links:
            linkfor = link.get_attribute('href')
            print(linkfor)
            sheet.append([linkfor])
            numberlink = numberlink + 1
        print("Найденно ссылок на товар:",numberlink)
        workbook.save("links.xlsx")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(0.2)
        buttonsled = driver.find_element(By.XPATH, '//*[@id="scroll-to"]/div[4]/div[2]/li[7]')
        sleep(0.1)
        buttonsled.click()
        sleep(4)
    except:
        pass
#driver.quit()