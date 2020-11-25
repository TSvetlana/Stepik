# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:04:34 2020

@author: Sveta
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_id("num1").text
    input2 = browser.find_element_by_id("num2").text
    summ=str(int(input1)+int(input2))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(summ)


    button= browser.find_element_by_xpath("//button[text()='Submit']");
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()