from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# webdriver managaer automatically downlaods the correct chromedriver elimintatinf need for manual updatesd
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/")
