import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)
    robot_check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robot_check.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_radio.click()
    click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    click_submit.click()

finally:
    time.sleep(5)
    browser.quit()


