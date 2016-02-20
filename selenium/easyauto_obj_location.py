# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

# location by id
# browser.find_element_by_id("kw").send_keys("selenium1")

# location by name
# browser.find_element_by_name("wd").send_keys("selenium2")

# location by tag name
# browser.find_element_by_tag_name("input").send_keys("selenium3")

# location by class name
# browser.find_element_by_class_name("s_ipt").send_keys("selenium4")

# location b""y css
# browser.find_element_by_css_selector("#kw").send_keys("selenium4")

# location by xpath
# browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("selenium5")

browser.find_element_by_link_text("贴吧").click()

# browser.find_element_by_id("su").click()
time.sleep(3)
print browser.title
browser.quit()