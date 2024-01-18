import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

    # cookies download
# browser = webdriver.Firefox()
# browser.maximize_window()
# browser.get('https://github.com/login')
# time.sleep(5)
# log = browser.find_element(By.XPATH, '//*[@id="login_field"]')
# log.send_keys('Enter log')
# passw = browser.find_element(By.XPATH, '//*[@id="password"]')
# passw.send_keys('enter pass')
# browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[13]').click()
# time.sleep(60)
# pickle.dump(browser.get_cookies(), open('gitcook', 'wb'))
# print('cookies saved')

    #cookies apply
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://github.com')
time.sleep(5)
for cookie in pickle.load(open('gitcook', 'rb')):
    browser.add_cookie(cookie)
time.sleep(20)
print('cookies uploaded')
browser.refresh()
