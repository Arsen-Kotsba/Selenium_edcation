from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

good_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
book_button = browser.find_element(By.ID, "book")
book_button.click()
x = browser.find_element(By.ID, "input_value")
result = calc(x.text)
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(result)
click_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
click_submit.click()
alert = browser.switch_to.alert
print(alert.text)