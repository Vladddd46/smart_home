import json

from flask import Flask, render_template, request

from adaptors.adaptors import jsonToCommand
from entities.SmartHomeController import SmartHomeController

app = Flask(__name__)

controller = SmartHomeController()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/control", methods=["POST"])
def handle_data():
    json_input = request.form.get("jsonInput")

    try:
        json_data = json.loads(json_input)
        requested_command = jsonToCommand(json_data)
        response = controller.handle_command(requested_command)
        registered_devices = controller.get_registered_devices()
        return render_template("index.html", data=registered_devices)
    except json.JSONDecodeError:
        return "Invalid JSON", 400
    except Exception as e:
        return f"Invalid '{e}'", 400

if __name__ == "__main__":
    app.run(debug=True)
