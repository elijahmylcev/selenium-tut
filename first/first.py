from selenium import webdriver
from config import executable_path
import time

url = 'https://www.instagram.com'
driver = webdriver.Chrome(executable_path=executable_path)

try:
    driver.get(url=url)
    driver.save_screenshot('1.png')

    time.sleep(3)

    # Полезно для разгадывания капчи
    # driver.refresh()
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
