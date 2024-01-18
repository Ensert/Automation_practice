import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', 'example')
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('marionette.port', 2828)
browser = webdriver.Firefox(options=option)
#browser.get('https://www.whatsmyua.info/')
browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
time.sleep(100)
#r