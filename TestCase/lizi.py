from selenium import webdriver
import time

driver = webdriver.Ie()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(10)
driver.close()

