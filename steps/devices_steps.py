from pytest_bdd import scenario, given, when, then, parsers
import pytest
from Firmware.BTM.modules import *
import os

@given(parsers.parse('I have connected a X2 with SN <module_sn>'))
def connected_X2(context, module_sn):
    context.moduleX2 = ModuleX2(module_sn)

@given(parsers.parse("I have checked connection of sensor <sensor_sn>"))
def check_sensor_connection(context, sensor_sn) -> None:
    sensors = context.moduleX2.get_sensor_list()
    assert (len(sensors) > 0 and sensors[0]['probe_sn'] == sensor_sn)

@when(parsers.parse("I have sent init packet"))
def sent_init_packet(context) -> None:
    assert context.moduleX2.sent_init_packet()

@then(parsers.parse("I have checked mission configuration period value is <period_value>"))
def check_mission_configuration(context, period_value) -> None:
    mission_config = context.moduleX2.get_mission_configuration()
    times = 10
    while (mission_config is None) and (times > 0):
        context.moduleX2.sent_init_packet()
        mission_config = context.moduleX2.get_mission_configuration()
        times -= 1
    assert mission_config["period"] is int(period_value)