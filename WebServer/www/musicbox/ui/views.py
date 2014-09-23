from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify
import happybase
import json


DEBUG = True
SECRET_KEY = 'fjl34f4984fkl43#(p'
SERVER_NAME = 'davidbianco.net'

app = Flask(__name__)
#app.config.from_object('wedding_site.app.config')

#from models import db
#db.init_app(app)

#from flask_mail import Mail
#mail = Mail(app)

#if not app.debug:
    #import logging
    #from logging.handlers import SMTPHandler
    #mail_handler = SMTPHandler('mail.trikeorama.com',
                               #'david&carolyn@trikeorama.com',
                               #'notice@davidbianco.net',
                               #'Wedding Website ERROR',
                               #('david&carolyn@trikeorama.com','trimailcycle'))
    #mail_handler.setLevel(logging.WARNING)
    ##app.logger.addHandler(mail_handler)
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


@app.route("/listen", methods=['GET', 'POST'])
@app.route("/listen/<event>", methods=['GET', 'POST'])
def listen(event=False):
    if request.method == 'POST':
        d = {}
        d['userid'] = 'fdj8a97sf'
        d['timestamp'] = 'Fri Sep 19 20:22:04 2014'
        d['songid'] = 'TRO786TE769'
        d['ip4'] = '23.123.3.24'
        event_json = ''
        if event == 'tup':
            d['event'] = event
            event_json = json.dumps(d, indent=4, separators=(',', ': '))
        if event == 'tdn':
            d['event'] = event
            event_json = json.dumps(d, indent=4, separators=(',', ': '))
        if event == 'skip':
            d['event'] = event
            event_json = json.dumps(d, indent=4, separators=(',', ': '))
        if event == 'pause':
            d['event'] = event
            event_json = json.dumps(d, indent=4, separators=(',', ': '))
        return render_template('listen.html', event_json=event_json)
    return render_template('listen.html')


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
        d = {}
        d['userid'] = 'r3kj4f2'
        d['event'] = 'login'
        d['timestamp'] = '2014'
        d['ip4'] = '131.143.1.123'
        return jsonify(userid=d['userid'],
                    event=d['event'],
                    timestamp=d['timestamp'],
                    ip4=d['ip4'])
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=debug)


