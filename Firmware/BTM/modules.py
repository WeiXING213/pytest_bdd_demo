from datetime import time
from Devices.BTM import commands
import Communication.ble as ble
from Communication.ble import ble_parameters
from Devices import types
import sys


class ModuleX2(object):

    def __init__(self, sn) -> None:
        sys.argv.append("-sn")
        sys.argv.append(str(sn))
        ble_parameters.parse()
        self.sn = sn

    def get_sensor_list(self) -> list:
        with ble.BLE(ble_parameters.get_serial_port()) as theBLE:
            ble_parameters.connect_to_ble_device(theBLE)
            with commands.commands(theBLE) as theCmd:
                return theCmd.read_sensor_list(aReadMode=types.SensorListReadMode.Measure | types.SensorListReadMode.NotInMission | types.SensorListReadMode.InMission)

    def sent_init_packet(self) -> bool:
        with ble.BLE(ble_parameters.get_serial_port()) as theBLE:
            ble_parameters.connect_to_ble_device(theBLE)
            with commands.commands(theBLE) as theCmd:
                return theCmd.send_init_packet()

    def get_mission_configuration(self) -> dict:
        with ble.BLE(ble_parameters.get_serial_port()) as theBLE:
            ble_parameters.connect_to_ble_device(theBLE)
            with commands.commands(theBLE) as theCmd:
                return theCmd.read_mission_config(channel_id=0)
