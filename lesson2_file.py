from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path = '/Users/mendovitskaya/environments/selenium_env/Scripts/chromedriver')
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("i.petrov@mail.ru")

file=browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
file.send_keys(file_path)


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


