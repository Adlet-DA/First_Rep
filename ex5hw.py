from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://yandex.kz/")
driver.implicitly_wait(3)
elem = driver.find_element(by=By.CLASS_NAME, value="weather__header")
link = elem.get_attribute('href')
elem.click()
print(elem.text)
print(link)

