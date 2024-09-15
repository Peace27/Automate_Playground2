from selenium.webdriver.common.by import By


class PlayGroundLocatorsPage:
    USERNAME = (By.NAME, "email-name")
    PASSWORD = (By.NAME, "password-name")
    LOGIN_BUTTON = (By.NAME, "submit-name")


class ClickNewCustomerLocatorsPage:
    NEW_CUSTOMER = (By.XPATH, "/html/body/div/a")


class AddNewCustomerLocators:
    EMAIL_ADDRESS = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.ID, "City")
    STATE = (By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/select")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/section/div/div/div/div/form/button")
