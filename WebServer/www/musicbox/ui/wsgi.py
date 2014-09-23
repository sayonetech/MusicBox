from flask import Flask
import os.path, sys

sys.path.append(os.path.dirname(__file__))

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

import views

if __name__ == '__main__':
    app.run()
