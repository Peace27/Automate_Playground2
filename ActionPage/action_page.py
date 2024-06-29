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
