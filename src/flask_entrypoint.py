# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, avem Python intrun Docker container!'

@app.route('/health')
def health():
    return 'Aplicatzia merge ok!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)