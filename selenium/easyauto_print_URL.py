# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

url = "http://www.baidu.com"
print "Now access %s" %url
browser.get(url)
print browser.title
time.sleep(3)

browser.maximize_window()
print "Browser's window is the maximize!" 
time.sleep(3)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)

browser.get("http://m.mail.10086.cn")
browser.set_window_size(480, 800)
time.sleep(3)
# print browser.url
print browser.title

browser.back()
print browser.title

browser.forward()
print browser.title

browser.quit()