import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestGoogleLogin:
    driver = ''

    def setup_method(self):
        url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url=url)

    def test_google_login_wright(self):
        search = self.driver.find_element(By.ID,"identifierId")
        search.send_keys('some text', Keys.ENTER)
        expected_text ='Електронна адреса або номер телефону'
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='aCsJod oJeWuf']").text
        time.sleep(5)
        assert expected_text == actual_text, f'Error. Expected text:{expected_text},but actual text: {actual_text}'

    def test_google_login_wrong(self):
        search = self.driver.find_element(By.ID,"identifierId")
        search.send_keys('some text', Keys.ENTER)
        expected_text ='Електронна адреса або номер телефону'
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='aCsJod oJeWuf']").text
        time.sleep(5)
        assert expected_text == actual_text, f'Error. Expected text:{expected_text},but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()