import time
import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_properties import ReadConfig


class Test00Login:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Nives-Admin-Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        account_btn = self.lp.return_account_btn()
        time.sleep(3)

        if account_btn.is_displayed():
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

