import time

from selenium.webdriver.common.by import By

from Project1.Base.base_class import Basedriver
from Project1.Utilities.utils import Utils


class Loginpage(Basedriver):

    # log = Utils.getLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    EMAIL_Field = "//input[@id = 'email']"
    PASS_Field = "//input[@id = 'pass']"
    LOGIN_Field = "//button[@name= 'login']"

    def email(self, gmail):
        email = self.driver.find_element(By.XPATH, self.EMAIL_Field)
        email.send_keys(gmail)

    def passwd(self, pswd):
        password = self.driver.find_element(By.XPATH, self.PASS_Field)
        password.send_keys(pswd)

    def login(self):
        login = self.driver.find_element(By.XPATH, self.LOGIN_Field)
        login.click()
        time.sleep(1)
        self.driver.back()

    def signin(self, gmail, pswd):
        self.email(gmail)
        self.passwd(pswd)
        self.login()
