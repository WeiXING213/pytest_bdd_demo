from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """main page locators"""
    GO_BUTTON = (By.ID, 'submit')

class LoginPageLocators(object):
    SUBMIT_BTN = (By.CLASS_NAME, 'submit')
    LOGIN_ERROR_USER_NOT_FOUND = (By.XPATH, "//*[text()='User not found.']")
    LOGIN_ERROR_INVALID_CREDENTIALS = (By.XPATH, "//*[text()='Invalid credentials.']")


class SideBarLocators(object):
    DEVICES_BTN = (By.XPATH, "//*[@class='sidebar']//*[@id='devices']")

class SearchResultsPageLocators(object):
    """search result locator"""
    pass

class ContentPageLocators(object):
    DATALOGGER_TABLE = (By.XPATH, "//*[@id='app-router-outlet-container']//*[@class='ui-table-tbody']//*[@class='designation-text']")
    START_BTN = (By.TAG_NAME, "mtv-toggle-mission-button")

class StartDataLoggingDialogLocators(object):
    SEND_BTN = (By.XPATH, "//button[.='Send']")
    START_BTN = (By.XPATH, "//button[.='Start']")