from entities.definitions import Function
from entities.Device import Device



class SmartHomeController:
	def __init__(self):
		self._devices = []

	def get_registered_devices(self):
		return self._devices

	def debug_print_registered_devices(self):
		print("registered_devices=", self._devices)

	def add_device(self, new_device: Device):
		self._devices.append(new_device)

	def register_device_command(self, params_json):
		keys = ["ip", "port", "name"]
		for i in keys:
			if i not in params_json.keys():
				print(f"Param {i} is missing")
				return None
		new_device = Device(name=params_json["name"], mac_address="", ip=params_json["ip"], port=params_json["port"])
		self.add_device(new_device)

	def turn_on_off_command(self, params_json):
		device_found = None
		for i in self._devices:
			if i._ip == params_json['ip'] and i._port == params_json['port']:
				device_found = i
				break

		if device_found != None:
			if params_json['action'] == "ON":
				device_found.turn(True)
			else:
				device_found.turn(False)
		else:
			print("Device not found")


	def handle_command(self, command):
		if command.function == Function.REGISTER_DEVICE.name:
			self.register_device_command(command.params)
		elif command.function == Function.TURN_ON_OFF.name:
			self.turn_on_off_command(command.params)
		else:
			print("Unknown function")
		self.debug_print_registered_devices()
		return {"result": "OK", "message": command.to_json()}
