from entities.Device import Device
from entities.definitions import Switch

class RosetteDevice(Device):

	def __init__(self, name, mac_address):
		super().__init__(name, mac_address)


	def turn(switch: Switch):
		print(f"turn {self.name}: ", switch)