from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    to_click = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    to_click.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)
    click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    click_submit.click()
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()