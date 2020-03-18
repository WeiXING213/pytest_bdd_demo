from pytest_bdd import scenario, given, when, then, parsers, scenarios
from selenium import webdriver
from pageObjects import page
import sys

sys.path.append("..")
from exceptions.oceaview_exceptions import *

# Given Steps
@given(parsers.cfparse('I have navigated to Oceaview with url {aUrl}'))
@given('I have navigated to Oceaview with url <aUrl>')
def givenNavigateToOceaViewPage(context, chromeBrowser, aUrl):
    context.loginPage = page.LoginPage(chromeBrowser).gotoUrl(aUrl)


@given(parsers.parse('I have entered <userName> into the user name'))
def givenIHaveEnteredSomethingIntoTheUserName(get_config, context, userName):
    context.loginPage.userNameInput_element = get_config.name if (get_config and userName == '<default>') else userName
    pass

@given(parsers.parse('I have entered <password> into the password'))
def givenIHaveEnteredSomethingIntoPassword(get_config, context, password):
    context.loginPage.passwordInput_element = password


# When steps

@when(parsers.parse('I have started data logging for sensor <sensor_sn_CRC> from module <module_sn>'))
def start_dataloging(context, sensor_sn, module_sn):
    start_data_logging_dialog = context.loginPage.sideBar.open_devices().click_module(module_sn)
    start_data_logging_dialog.password_input_element = "Oceasoft123@"
    start_data_logging_dialog.click_send_button().click_start_button()


@when("I press submit button")
def press_submit_button(context):
    try:
        context.loginPage = context.loginPage.click_logIn_button()
        assert context.loginPage is not None
        return
    except OceaViewUserNotFoundException:
        context.currentException = OceaViewUserNotFoundException
    except OceaViewInvalidCredentialException:
        context.currentException = OceaViewInvalidCredentialException
    else:
        raise NotImplemented


@then("Login should fail")
def check_login_expected_exception(context):
    assert ((context.currentException is not None)
            or (context.currentException is OceaViewUserNotFoundException)\
            or (context.currentException is OceaViewInvalidCredentialException))\
           is True
