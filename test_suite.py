import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.action_page import PlayGroundActionsPages, AddNewCustomerActionsPage, ClickNewCustomerActionsPage
from Config.config import Config


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # Uncomment the line below to run in headless mode
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = PlayGroundActionsPages(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page


def test_login_page_on_automation_play_ground_website(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_login()


def test_click_new_customer(login):
    test_click_new_customer = ClickNewCustomerActionsPage(login.driver)
    test_click_new_customer.Click_New_Customer()


def test_add_new_customer_form(login):
    test_add_new_customer_form = AddNewCustomerActionsPage(login.driver)
    test_add_new_customer_form.enter_email_address(Config.EMAIL_ADDRESS)
    test_add_new_customer_form.enter_first_name(Config.FIRST_NAME)
    test_add_new_customer_form.enter_last_name(Config.LAST_NAME)
    test_add_new_customer_form.enter_city(Config.CITY)
    test_add_new_customer_form.enter_state()
    test_add_new_customer_form.click_submit_button()
