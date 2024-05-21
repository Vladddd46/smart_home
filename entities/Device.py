from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, name, mac_address):
        self._name = name
        self._mac_address = mac_address

    @abstractmethod
    def some_abstract_method(self):
        # TODO will add soon
        pass
