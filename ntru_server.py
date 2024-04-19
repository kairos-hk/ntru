from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/enc', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')

    command = ['python3', 'NTRU.py', '-k', 'NTRU_key', '-eS', text, '-T']
    
    try:
        process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        return jsonify({'result': output})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'ntru.py 실행 중 오류 발생: {e}'})

@app.route('/dec', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')

    command = ['python3' 'NTRU.py', '-k', 'NTRU_key', '-T', '-dS', text,]
    
    try:
        process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        return jsonify({'result': output})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'ntru.py 실행 중 오류 발생: {e}'})

if __name__ == '__main__':
    app.run(debug=True)
