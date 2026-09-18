from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(3)

driver.get("https://www.youtube.com")

time.sleep(3)

driver.back()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.refresh()

time.sleep(3)

driver.quit()