import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

_id = os.getenv('ID')
path_brawser = os.getenv('PATH_BROWSER')
path_driver = os.getenv('PATH_DRIVER')
url = os.getenv('URL')

options = Options()
options.binary_location = path_brawser
driver_path = path_driver
drvr = webdriver.Chrome(options = options, executable_path = driver_path)
drvr.get(url)
time.sleep(30)