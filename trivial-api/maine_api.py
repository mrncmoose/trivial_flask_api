'''
Created on Oct 28, 2019

@author: moose
'''
#!flask/bin/python
from flask import Flask, jsonify, request, Response
from functools import wraps

app = Flask(__name__)
def cToF(tempVal):
    return tempVal * 1.8 +32

def fToC(tempVal):    
    return (tempVal - 32)/1.8

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'change-me!'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def getCurrentTemp():
    return '42F';

@app.route('/thermal/api/v1.0/current_temp', methods=['GET'])
@requires_auth
def get_current_temp():
    current_temp = getCurrentTemp()
    return jsonify({'current_temp': current_temp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
