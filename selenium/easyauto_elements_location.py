# # coding=utf-8
# from selenium import webdriver
# import time
# import os

# browser = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('checkbox.html')
# browser.get(file_path)

# inputs = browser.find_element_by_tag_name('input')
# for input in inputs:
# 	if input.get_attribute('type') == 'checkbox':
# 		input.click()
# time.sleep(3)

# browser.quit()
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Firefox()
file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

# 选择所有的checkbox并全部勾上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

# 打印当前页面上有多少个checkbox
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))
time.sleep(2)

dr.quit()