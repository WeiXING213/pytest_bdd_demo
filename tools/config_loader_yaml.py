from __future__ import annotations
import yaml
from abc import ABCMeta, abstractmethod

class yaml_object_interface(metaclass=ABCMeta):
    @abstractmethod
    def to_yaml_stream(self):
        pass

class yaml_object(yaml_object_interface):
    def to_yaml_stream(self):
        return yaml.dump(self.__dict__)

class OceaViewUserConfiguration(yaml_object):
    def __init__(self, name=None, password=None):
        self._name = name
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @staticmethod
    def get_object_from_stream(stream) -> OceaViewUserConfiguration:
        """load object from yaml format stream"""
        values = yaml.safe_load(stream)
        return OceaViewUserConfiguration(values["_name"], values["_password"])

    @staticmethod
    def get_object_from_file(file_name) -> OceaViewUserConfiguration:
        """load object from a yaml format file """
        with open(file_name, mode='r') as file:
            values = yaml.load(file, Loader=yaml.FullLoader)
            return OceaViewUserConfiguration(values["_name"], values["_password"])
