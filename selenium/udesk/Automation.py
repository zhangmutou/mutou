from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://rd-dota.udesk.cn")
time.sleep(2)
# access to loginPage
browser.find_element_by_class_name("login").click()
# input username,password
browser.find_element_by_id("user_email").send_keys("zhangmutou44@163.com")
browser.find_element_by_id("user_password").send_keys("zs123456")
browser.find_element_by_name("commit").click()
time.sleep(10)
# access to callcenter
browser.find_element_by_xpath("//*[@id="ember865"]/a/span").click()

browser.quit()