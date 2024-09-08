import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locators_pages import PlayGroundLocatorsPage, AddNewCustomerLocators


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


class AddNewCustomer:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)
        time.sleep(5)

    def enter_first_name(self, first_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.FIRST_NAME))
        enter_first_name.send_keys(first_name)
        time.sleep(5)

    def enter_last_name(self, last_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.LAST_NAME))
        enter_first_name.send_keys(last_name)
        time.sleep(5)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(10)

    def enter_state(self):
        enter_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.STATE))
        enter_state.click()
        time.sleep(10)


