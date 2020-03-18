from pytest_bdd import scenario, given, when, then, parsers, scenarios
from selenium import webdriver
from pageObjects import page
import pytest
import sys
from .devices_steps import *
from .pages_steps import *

CONVERTERS = {
    'aUrl': str,
    'userName': str,
    'password': str,
    'module_sn':str,
    'sensor_sn':str,
    'sensor_sn_CRC':str,
    'period_value':str,
}

# Scenarios
#scenarios('start_data_logging.feature', example_converters=CONVERTERS)
scenarios('.', example_converters=CONVERTERS)