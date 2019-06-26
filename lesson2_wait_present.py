import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(executable_path = 'C:/Users/m.endovitskaya/environments/selenium_env/Scripts/chromedriver', chrome_options=opt)
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )

book = browser.find_element_by_id("book")
book.click()

input = browser.find_element_by_id("input_value")
input_text = input.text
x = input_text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

send = browser.find_element_by_id("solve")
send.click()

