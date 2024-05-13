from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pyflowchart import Flowchart
import PyComponent

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/convert', methods=['POST'])
def convert_to_html():
    data = request.json
    code = data['code']
    result = PyComponent.analyze_python_code(code)
    return result

if __name__ == '__main__':
    app.run(debug=True)
