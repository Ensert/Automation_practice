# start for web tests
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestGoogleLogin:
    search_words = ('Електронна адреса або номер телефону', 'електронна адреса або номер телефону', 'Електронна адреса або номер телефону')
    driver = ''

    def setup_method(self):
        url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url=url)

    @pytest.mark.parametrize('search_query', search_words)
    def test_google_login(self, search_query):

        search = self.driver.find_element(By.ID, "identifierId")
        search.send_keys('fake pass', Keys.ENTER)
        expected_text = search_query
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='aCsJod oJeWuf']").text
        time.sleep(5)
        assert expected_text == actual_text, f'Error. Expected text:{expected_text},but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()
#R
