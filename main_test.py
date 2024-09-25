import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.sbis.ru")

contacts_link = driver.find_element(By.LINK_TEXT, "Контакты")
contacts_link.click()

banner_link = driver.find_element(By.XPATH, "//a[@href='https://tensor.ru/']")
banner_link.click()

#people_block = driver.find_element(By.XPATH, "//p[contains(@class, "
#                                  "'tensor_ru-Index__card-title') and contains(@class, 'tensor_ru-pb-16')]")

about_button = driver.find_element(By.LINK_TEXT, "Подробнее")
about_button.click()
time.sleep(5)
driver.quit()
