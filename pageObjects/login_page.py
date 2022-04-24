from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_email_id = "email_section"
    textbox_password_id = "password_section"
    button_login_xpath = '//*[@id="root"]/div/div/div/form/div[4]/button'
    button_account_xpath = '//*[@id="root"]/div/div[1]/div/button'
    link_logout_xpath = '//*[@id="root"]/div/div[1]/div/div/button[1]/a'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        # verify email text element is displayed by explicit wait
        try:
            email_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.textbox_email_id))
            )
            email_element.clear()
            email_element.send_keys(email)

        finally:
            pass

    def set_password(self, password):
        # verify password text element is displayed by explicit wait
        try:
            password_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.textbox_password_id))
            )
            password_element.clear()
            password_element.send_keys(password)

        finally:
            pass

    def click_login(self):
        # verify login btn element is displayed by explicit wait
        try:
            login_btn_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.button_login_xpath))
            )
            login_btn_element.click()
        finally:
            pass

    def click_account(self):
        # verify account btn element is displayed by explicit wait
        try:
            button_account_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.button_account_xpath))
            )
            button_account_element.click()
        finally:
            pass

    def click_logout(self):
        # verify logout btn element is displayed by explicit wait
        try:
            logout_btn_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.link_logout_xpath))
            )
            logout_btn_element.click()
        finally:
            pass

    def return_account_btn(self):
        # verify account button element is displayed by explicit wait
        try:
            account_btn_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.button_account_xpath))
            )
            return account_btn_element
        finally:
            pass
