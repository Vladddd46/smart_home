import requests

url = 'http://127.0.0.1:5000/control'

data = {
    "domain": "light",
    "area": "room_1",
    "action": "turn_on",
    "params": {"device_id": 0}
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
