import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://play.upland.me/login')
time.sleep(4)
#go_to_log = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[2]/div[1]/div/div[3]/button').click()
log = driver.find_element(By.XPATH, '//*[@id="email-field"]')
time.sleep(1)
log.send_keys('makcmaksymiv@gmail.com')
password = driver.find_element(By.XPATH, '//*[@id="root"]/div[9]/div/div/div[2]/div[1]/div/div/div/div/form/div[2]/input')
password.send_keys('Aemua11111', Keys.ENTER)
time.sleep(10)

# no resolved yet
