import time
import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test001Login:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_homepage_title(self, setup):

        self.logger.info("********** Test001Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Nives-Admin-Dashboard":
            assert True
            self.driver.close()
            self.logger.info("********** Home page title test pass **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("********** Home page title test failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        account_btn = self.lp.return_account_btn()
        time.sleep(3)

        if account_btn.is_displayed():
            assert True
            self.logger.info("********** Login test passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********** Login test failed **********")
            assert False

