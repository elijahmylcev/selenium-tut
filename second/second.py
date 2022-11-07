from selenium import webdriver
from config import executable_path
from fake_useragent import UserAgent
import random
import time

# "Сырые строки" создаются префексом r для windows
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# user_agent_list = [
#     'text',
#     'examples'
# ]
useragent = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Hello World")
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")
options.add_argument(f"user-agent={useragent.random}")


driver = webdriver.Chrome(
    executable_path=executable_path,
    options=options
)

try:
    driver.get(url=url)
    driver.save_screenshot('./1.png')

    time.sleep(3)

    # Полезно для разгадывания капчи
    # driver.refresh()
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
