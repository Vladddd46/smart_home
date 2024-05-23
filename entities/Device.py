
class Device():
    def __init__(self, name, mac_address, ip, port):
        self._name = name
        self._mac_address = mac_address
        self._ip = ip
        self._port = port


    def turn(self, on: bool):
    	print("IMPLEMENT TURN LOGIC")
    	print(f"turn {on}")


    def __str__(self):
        return f"Device(name={self._name}, ip={self._ip}, port={self._port})"

    def __repr__(self):
        return f"Device(name={self._name}, ip={self._ip}, port={self._port})"