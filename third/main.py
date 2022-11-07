from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from config import executable_path, url
from fake_useragent import UserAgent
import random
import time

useragent = UserAgent()
receiving = 1000

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(
    executable_path=executable_path,
    options=options
)

try:
    driver.get(url=url)
    time.sleep(2)

    select_country = driver.find_element(By.CLASS_NAME, 'select__indicators')
    select_country = select_country.click()
    # select_country = driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys('value="KAZ"')
    KAZ = driver.find_element(By.ID, 'changeable-field-select-option-KAZ')
    KAZ.click()
    time.sleep(4)
    sum = driver.find_element(By.ID, 'changeable-field-input-amount')
    sum.send_keys(receiving)

    select_currency = driver.find_elements(By.CLASS_NAME, 'select__control')
    select_currency = select_currency[2].click()
    KAZ_currency = driver.find_element(By.ID, 'react-select-4-option-1')
    KAZ_currency.click()
    time.sleep(2)
    #CheckBox_checkbox-input___BTr3
    driver.find_element(By.CLASS_NAME, 'CheckBox_checkbox-input___BTr3').click()
    time.sleep(2)

    to_pay = driver.find_element(By.CLASS_NAME, 'static-text-calculatorAmount')

    print(to_pay.text)

    with open('ind.html', 'w') as f:
        f.write(web_page_source)
    #
    time.sleep(3)


except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
