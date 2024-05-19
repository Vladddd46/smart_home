from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask server!"

@app.route('/control', methods=['POST'])
def handle_data():
    if request.is_json:
        data = request.get_json()
        print("Received data: ", data)
        return jsonify({"result_code": "OK", "message": ""}), 200
    else:
        return jsonify({"result_code": "WRONG_FORMAT", "message": "request must be json"}), 400

if __name__ == '__main__':
    app.run(debug=True)
