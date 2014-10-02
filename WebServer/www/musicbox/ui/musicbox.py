from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify
import happybase
import json
import subprocess
import os
import datetime
from time import gmtime, strftime
from kafka import KafkaClient, SimpleProducer

kafka = KafkaClient('cluster.davidbianco.net:8092')
producer = SimpleProducer(kafka)
kafka_topic = "event_log"

connection = happybase.Connection('cluster.davidbianco.net')

DEBUG = True
SERVER_NAME = 'davidbianco.net'

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True
#app.server_name = 'davidbianco.net'

#app.config.from_object('wedding_site.app.config')

#from models import db
#db.init_app(app)

#from flask_mail import Mail
#mail = Mail(app)

#if not app.debug:
    #import logging
    #from logging.handlers import SMTPHandler
#
    #file_handler = logging.FileHandler('/var/log/flask/weberror.log')
    #file_handler.setLevel(logging.WARNING)
    #app.logger.addHandler(file_handler)
#
    #file_handler.setFormatter(logging.Formatter(
        #'%(asctime)s %(levelname)s: %(message)s '
        #'[in %(pathname)s:%(lineno)d]'
    #))


connection = happybase.Connection('cluster.davidbianco.net')

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/user/<userid>/<event>")
def non_listen(userid=False, event=False):
    if event == 'search':
        pass
    elif event == 'exit':
        pass

@app.route("/event", methods=['POST'])
def event():
    response = {"status": "OK"}
    userid = request.form['userid']
    event = request.form['event']
    songid = request.form['songid']
    print userid, event, songid
    return jsonify(response)


@app.route("/listen", methods=['GET', 'POST'])
@app.route("/listen/user/<userid>/<event>", methods=['GET', 'POST'])
@app.route("/listen/user/<userid>/<event>/song/<songid>", methods=['GET', 'POST'])
def listen(userid=False, event=False, songid=False):
    ''' tup, tdn, skip, pause, play '''
    #if request.method == 'POST':
    message = {}
    #message['userid'] = 'fdj8a97sf'
    #message['timestamp'] = 'Fri Sep 19 20:22:04 2014'
    message['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #message['songid'] = 'TRO786TE769'
    message['ip4'] = '23.123.3.24'
    message['event'] = event
    message['songid'] = songid
    #event_json = ''
    event_json = json.dumps(message, indent=4, separators=(',', ': '))
    producer.send_messages(kafka_topic, event_json)
    if event == 'tup':
        message['event'] = event
        event_json = json.dumps(d, indent=4, separators=(',', ': '))
    elif event == 'tdn':
        message['event'] = event
        event_json = json.dumps(d, indent=4, separators=(',', ': '))
    elif event == 'skip':
        message['event'] = event
        event_json = json.dumps(d, indent=4, separators=(',', ': '))
    elif event == 'pause':
        message['event'] = event
        event_json = json.dumps(d, indent=4, separators=(',', ': '))
    elif event == 'play':
        message['event'] = event
        pass
    data = {}
    data['userid'] = 'Me'
    data['songid'] = 'TRFDK834879DFDS3F'
    #return render_template('listen.html', event_json=event_json)
    return render_template('listen.html', data=data)
    #return render_template('listen.html')


@app.route("/")
@app.route("/search", methods=['GET', 'POST'])
@app.route("/search/<q>", methods=['GET', 'POST'])
def search(q=False):
    if request.method == 'POST':
        return jsonify(test='test')
    return render_template('search.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        message = {}
        message['userid'] = 'r3kj4f2'
        message['event'] = 'login'
        message['timestamp'] = '2014'
        message['ip4'] = '131.143.1.123'
        return jsonify(userid=message['userid'],
                    event=message['event'],
                    timestamp=message['timestamp'],
                    ip4=message['ip4'])
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = '8fd9qio23l23fp'
        fname = 'David'
        lname = 'Bianco'
        event = 'register'
        timestamp = '2014'
        ip4 = '23.14.53.64'
        email = 'test@example.org'
        gender = 'M'
        zipcode = '93252'
        birth_year = '1998'

        return jsonify(userid=userid,
                fname=fname, lname=lname,
                email=email, gender=gender,
                zipcode=zipcode, birth_year=birth_year,
                timestamp=timestamp, ip4=ip4, event=event)

    return render_template('register.html')

@app.route("/view-events")
def view_events():
    logfile = "/var/log/events.log"
    events = subprocess.Popen(['tail', '-80', logfile], stdout = subprocess.PIPE).communicate()[0]
    return render_template('view-events.html', events=events)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=DEBUG)


