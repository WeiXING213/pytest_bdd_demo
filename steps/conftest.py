import pytest
from selenium import webdriver
import datetime
import os
import pytest
from tools.config_loader_yaml import OceaViewUserConfiguration

# Constants
BROWSER = None
IMAGE_PATH = "save_images"
OCEAVIEW_USER_CONFIG = None

# Hooks
def pytest_bdd_before_scenario(request, feature, scenario):
    """- Called before scenario is executed"""
    config_file = os.path.join(os.path.dirname(feature.filename), "config.yml")
    if os.path.exists(config_file):
        global OCEAVIEW_USER_CONFIG
        OCEAVIEW_USER_CONFIG = OceaViewUserConfiguration.get_object_from_file(config_file)
    pass

def pytest_bdd_after_scenario(request, feature, scenario):
    """- Called after scenario is executed (even if one of steps has failed)"""
    save_screen_file_name = datetime.datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%f") + ".JPG"
    image_saving_path = os.path.join("..",
                                     IMAGE_PATH,
                                     save_screen_file_name)
    BROWSER.save_screenshot(image_saving_path)
    BROWSER.quit()

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """- Called before step function is executed and it’s arguments evaluated"""
    pass

def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    """- Called before step function is executed with evaluated arguments"""
    pass

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    """- Called after step function is successfully executed"""
    pass

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """- Called when step function failed to execute, exception goes here, assert"""
    name = str(step.name).replace(" ", "_").replace("<", "_").replace(">", "_")
    image_saving_path = os.path.join("..",
                                     IMAGE_PATH,
                                     name + datetime.datetime.now().strftime("-%d-%b-%Y-%H-%M-%S-%f") + ".JPG")
    BROWSER.save_screenshot(image_saving_path)

def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """- Called when step failed to validate"""
    pass

def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    """- Called when step lookup failed"""
    pass

# Fixtures
@pytest.fixture
def context():
    class Context(object):
        pass
    return Context()

@pytest.fixture()
def get_config():
    global OCEAVIEW_USER_CONFIG
    return OCEAVIEW_USER_CONFIG

@pytest.fixture
def chromeBrowser():
    global BROWSER

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    BROWSER = webdriver.Chrome("..\\chromeDriver\\chromedriver.exe",
                               chrome_options=options)
    BROWSER.maximize_window()

    yield BROWSER