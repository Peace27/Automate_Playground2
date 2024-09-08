import pytest
from selenium import webdriver

from ActionPage.action_page import PlayGroundPages, AddNewCustomer


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = PlayGroundPages(driver)
    login_page.open_login_page("https://automationplayground.com/crm/login.html")
    return login_page


def test_login_page_on_automation_play_ground_website(login):
    login.enter_username("automation@gmail.com")
    login.enter_password("Password2@")
    login.click_login_button()
    login.click_new_customer()


def test_successful_login_redirects_to_dashboard(login):
    test_add_new_customer_form = AddNewCustomer(login.driver)
    test_add_new_customer_form.enter_email_address("email@gmail.com")
    test_add_new_customer_form.enter_first_name("Jacob")
    test_add_new_customer_form.enter_last_name("Othniel")
    test_add_new_customer_form.enter_city("Lagos")
    # test_add_new_customer_form.enter_state()
