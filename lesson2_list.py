from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome(executable_path = '/Users/mendovitskaya/environments/selenium_env/Scripts/chromedriver')
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
z=str(str(int(x)+int(y)))
print(z)

dropdown= browser.find_element_by_id("dropdown")
dropdown.click()

value=browser.find_element_by_css_selector("[value='" + z + "']").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()