from selenium.webdriver.support.ui import WebDriverWait

class BasePageElementCss(object):
    """base page class"""

    def __set__(self, obj, value):
        """set text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda x: x.find_element_by_css_selector(self.locator))
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda x: x.find_element_by_css_selector(self.locator))
        element = driver.find_element_by_css_selector(self.locator)

        return element.get_attribute("value")

class BasePageElement(object):
    """base page class"""

    def __set__(self, obj, value):
        """set text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda x: x.find_element_by_id(self.locator))
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda x: x.find_element_by_id(self.locator))
        element = driver.find_element_by_id(self.locator)

        return element.get_attribute("value")