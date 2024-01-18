import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

bro = webdriver.Chrome()
# bro.get('https://www.linkedin.com/in/sviatoslav-maksymiv-18626a175')
# time.sleep(5)
bro.get('https://www.youtube.com/')
# bro.save_screenshot('1.jpg')  #save screenshot
info = bro.find_elements(By.XPATH, '//*[@id="contents"]')
#button = bro.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
scroll = bro.find_element(By.TAG_NAME, 'html')
for i in range(10):
    scroll.send_keys(Keys.DOWN)

time.sleep(5)
#R