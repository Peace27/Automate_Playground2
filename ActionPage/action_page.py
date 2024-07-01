import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locators_pages import PlayGroundLocatorsPage



# URL
class PlayGroundPages:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    #
    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PlayGroundLocatorsPage.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PlayGroundLocatorsPage.PASSWORD))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PlayGroundLocatorsPage.LOGIN_BUTTON))
        click_login_button.click()

    def click_new_customer(self):
        click_new_customer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PlayGroundLocatorsPage.NEW_CUSTOMER))
        click_new_customer.click()

    def enter_emailaddress(self, email_address):
        pass


class AddNewCustomer:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomer.EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)
