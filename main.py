from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def handle_data():
    json_input = request.form.get('jsonInput')
    try:
        data = json.loads(json_input)
        return render_template('result.html', data=data)
    except json.JSONDecodeError:
        return "Invalid JSON", 400

if __name__ == '__main__':
    app.run(debug=True)
