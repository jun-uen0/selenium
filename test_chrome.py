from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://login.paypay-bank.co.jp/')
time.sleep(30)