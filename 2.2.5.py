# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:38:48 2020

@author: Sveta
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input2 = browser.find_element_by_id("input_value").text
    #input3=input2.get_attribute("valuex")

    input4 = browser.find_element_by_id("answer")
    input4.send_keys(calc(input2))

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

    option2 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button= browser.find_element_by_class_name("btn");
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()