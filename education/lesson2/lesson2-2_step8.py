from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys('Михайло')
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Потапыч')
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('mikhaylo@mail.ru')
    file_upload = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'step8_file.txt')
    file_upload.send_keys(file_path)
    click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    click_submit.click()

finally:
    browser.quit()