# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:56:21 2020

@author: Sveta
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input2 = browser.find_element_by_tag("img[src='images/chest.png']")
    input3=input2.get_attribute("[valuex='552']")
    print(input3)
    input4 = browser.find_element_by_id("answer")
    input4.send_keys(calc(input3))

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button= browser.find_element_by_xpath("//button[text()='Submit']");
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()