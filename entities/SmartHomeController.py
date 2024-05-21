from entities.definitions import Function

class SmartHomeController:
	def __init__(self):
		self._devices = []

	def register_device(self, params_json):
		print("register_device", params_json)

	def remove_device(self):
		print("remove_device")

	def turn_on_off(self):
		print("turn_on_off")

	def handle_command(self, command):
		if command.function == Function.REGISTER_DEVICE.name:
			self.register_device(command.params)
		elif command.function == Function.REMOVE_DEVICE.name:
			self.remove_device()
		elif command.function == Function.TURN_ON_OFF.name:
			self.turn_on_off()
		else:
			print("Unknown function")
		
		return {"result": "OK", "message": command.to_json()}
