import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
try:
    driver.get(url=url)
    search = driver.find_element(By.ID, "identifierId")
    search.send_keys('zalupa konia', Keys.ENTER)
    expected_text ='Електронна адреса або номер телефону'
    actual_text = driver.find_element(By.XPATH, "//div[@class='aCsJod oJeWuf']").text
    time.sleep(5)
    assert expected_text == actual_text, f'Error. Expected text:{expected_text},but actual text: {actual_text}'

finally:
    driver.close()
    driver.quit()

  #  $x("//span[@class='jibhHc']")
