import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.element import *
from pageObjects.locators import *
import sys
sys.path.append("..")
from exceptions.oceaview_exceptions import *

class OceaViewPasswordNotFoundException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'q'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class userNameInputElement(BasePageElement):
    locator = 'userName'

class passwordInputElement(BasePageElement):
    locator = 'password'

class passwordInputElement(BasePageElementCss):
    locator = 'input[formControlName=password]'

class LoginPage(BasePage):
    """login page"""
    userNameInput_element = userNameInputElement()
    passwordInput_element = passwordInputElement()

    def gotoUrl(self, aUrl):
        self.driver.get(aUrl)
        return self

    def check_login_error(self) -> None:
        # TODO add check other warnings such as  "This user account is locked.
        self.driver.implicitly_wait(3)
        self.check_login_user_error()
        self.check_login_password_error()

    def check_login_user_error(self) -> None:
        try:
            self.driver.find_element(*LoginPageLocators.LOGIN_ERROR_USER_NOT_FOUND)
        except NoSuchElementException:
            return
        raise OceaViewUserNotFoundException("wrong user name", "login")

    def check_login_password_error(self) -> None:
        try:
            self.driver.find_element(*LoginPageLocators.LOGIN_ERROR_INVALID_CREDENTIALS)
        except NoSuchElementException:
            return
        raise OceaViewInvalidCredentialException("wrong password", "login")

    def click_logIn_button(self):
        element = self.driver.find_element(*LoginPageLocators.SUBMIT_BTN)
        element.click()
        self.check_login_error()
        return MainPage(self.driver)

class SideBar(BasePage):
    def open_devices(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SideBarLocators.DEVICES_BTN))
        element.click()
        return ContentPage(self.driver)

class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.sideBar = SideBar(self.driver)

class ContentPage(BasePage):
    def click_module(self, module_sn):
        self.driver.implicitly_wait(5)
        elements = self.driver.find_elements(*ContentPageLocators.DATALOGGER_TABLE)
        result = next(element for element in elements if element.text.startswith(module_sn))
        result.click()
        #TODO new page

        btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(ContentPageLocators.START_BTN))
        btn.click()
        return StartDataLoggingDialog(self.driver)

class StartDataLoggingDialog(BasePage):
    password_input_element = passwordInputElement()

    def click_send_button(self):
        (self.driver.find_element(*StartDataLoggingDialogLocators.SEND_BTN)).click()
        return self

    def click_start_button(self):
        time.sleep(5)
        btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(StartDataLoggingDialogLocators.START_BTN))
        btn.click()