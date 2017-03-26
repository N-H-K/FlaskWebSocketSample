#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

##
# @file app.py
# @date 2017-03-26

from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('./view.html')

@app.route('/api/v1/start')
def start():
    print "start"
    send_to_hololens({'command': 'start'})
    return 'ok'

@socketio.on('connect', namespace='/main')
def handle_connect():
    print "connect"
    socketio.emit('pitagraswitch', {'data': 'connected'}, namespace='/main')

@socketio.on('json')
def handle_json(json):
    print 'recieved json %s' % str(json)

def send_to_hololens(data):
    print "sending.."
    print data
    socketio.emit('pitagoraswitch', data, broadcast=True, namespace='/main')
    print "done"

if __name__ == '__main__':
    socketio.run(app, debug=True)
    print "start"
