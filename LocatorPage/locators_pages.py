from selenium.webdriver.common.by import By


class PlayGroundLocatorsPage:
    USERNAME = (By.NAME, "email-name")
    PASSWORD = (By.NAME, "password-name")
    LOGIN_BUTTON = (By.NAME, "submit-name")
    NEW_CUSTOMER = (By.ID, "new-customer")


class AddNewCustomer:
    EMAIL_ADDRESS = (By.ID, "Email_Address")
