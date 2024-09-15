import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locators_pages import PlayGroundLocatorsPage, AddNewCustomerLocators, ClickNewCustomerLocatorsPage


# URL
class PlayGroundActionsPages:
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

    def click_login(self):
        click_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PlayGroundLocatorsPage.LOGIN_BUTTON))
        click_submit.click()
        time.sleep(1)


class ClickNewCustomerActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def Click_New_Customer(self):
        Click_New_Customer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickNewCustomerLocatorsPage.NEW_CUSTOMER))
        Click_New_Customer.click()
        time.sleep(2)


class AddNewCustomerActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)
        time.sleep(1)

    def enter_first_name(self, first_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.FIRST_NAME))
        enter_first_name.send_keys(first_name)
        time.sleep(1)

    def enter_last_name(self, last_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.LAST_NAME))
        enter_first_name.send_keys(last_name)
        time.sleep(1)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(1)

    def enter_state(self):
        enter_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.STATE))
        enter_state.click()
        time.sleep(1)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(1)
