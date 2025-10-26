from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.txt'

@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.json.get('data', '')
        
        with open(DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(data + '\n')
        
        return jsonify({'status': 'success', 'message': 'Data saved successfully'})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/read', methods=['GET'])
def read_data():
    try:
        if not os.path.exists(DATA_FILE):
            return jsonify({'status': 'success', 'data': []})
        
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        data_list = [line.strip() for line in lines if line.strip()]
        
        return jsonify({'status': 'success', 'data': data_list})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Создаем файл если его нет
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w').close()
    
    app.run(debug=True, host='0.0.0.0', port=5000)