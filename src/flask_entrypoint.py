# flask_web/app.py

        
import socket   
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)    
    return 'Hey, avem Python intrun Docker container in Kubernetes pe masina '+IPAddr+'!'

@app.route('/health')
def health():
    return 'Aplicatzia merge ok!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)