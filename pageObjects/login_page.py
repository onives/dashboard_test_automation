from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_email_id = "email_section"
    textbox_password_id = "password_section"
    button_login_xpath = '//*[@id="root"]/div/div/div/form/div[4]/button'
    button_account_xpath = '//*[@id="root"]/div/div[1]/div/button'
    link_logout_xpath = '//*[@id="root"]/div/div[1]/div/div/button[1]/a'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_account(self):
        self.driver.find_element(By.XPATH, self.button_account_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
