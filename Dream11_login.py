import pickle
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

chrome.get("https://www.dream11.com")
try:
    WebDriverWait(chrome, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='matchCardMainTitle_7b586 matchCardMainTitleDesktop_83a22']")))
finally:
    pass

pickle.dump(chrome.get_cookies(), open("cookie.txt","wb"))
