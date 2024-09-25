from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)
    click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", click_submit)
    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    click_submit.click()

finally:
    time.sleep(5)
    browser.quit()
