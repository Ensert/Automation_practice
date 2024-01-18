import  time
import  pickle
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://for-ua.com/')
time.sleep(60)
pickle.dump(browser.get_cookies(), open('session', 'wb'))
print('cookies saved')
time.sleep(10)
browser