from selenium.webdriver.common.by import By


class PlayGroundLocatorsPage:
    USERNAME = (By.NAME, "email-name")
    PASSWORD = (By.NAME, "password-name")
    LOGIN_BUTTON = (By.NAME, "submit-name")
    NEW_CUSTOMER = (By.ID, "new-customer")


class AddNewCustomerLocators:
    EMAIL_ADDRESS = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.ID, "City")
    STATE = (By.XPATH, "state")
    REGION = (By.XPATH, "region")




