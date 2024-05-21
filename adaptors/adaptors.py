from entities.Command import Command

def jsonToCommand(json_data: dict):
	keys = ["domain", "function", "params"]
	for i in keys:
		if i not in json_data.keys():
			print(f"Wrong format: missing '{i}' key")
			return None

	result = Command(json_data["domain"], json_data["function"], json_data["params"])
	return result