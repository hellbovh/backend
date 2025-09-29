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

if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w').close()
    
    app.run(debug=True, port=5000)