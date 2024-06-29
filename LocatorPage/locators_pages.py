from selenium.webdriver.common.by import By


class PlayGroundLocatorsPage:
    USERNAME = (By.NAME, "email-name")
    PASSWORD = (By.NAME, "password-name")
    LOGIN_BUTTON = (By.ID, "submit-name")
