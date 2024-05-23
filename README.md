
run server: python main.py

Now communication with server is done via json messages.

1. First you need to register device: 
{"domain": "GENERAL", "function": "REGISTER_DEVICE", "params": {"ip": "127.0.0.1", "port": 5005, "name": "device_1"}}

2. Then you can turn [on/off] it.
{"domain": "GENERAL", "function": "TURN_ON_OFF", "params": {"ip": "127.0.0.1", "port": 5005, "action": "ON"}}