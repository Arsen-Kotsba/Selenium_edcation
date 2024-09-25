from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "treasure")
    result = calc(x.get_attribute("valuex"))
    print(x.get_attribute("valuex"))
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)
    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    click_submit.click()

finally:
    time.sleep(1)
    browser.quit()