from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify
import happybase
import json


DEBUG = True
SECRET_KEY = 'fjl34f4984fkl43#(p'
SERVER_NAME = 'davidbianco.net'

app = Flask(__name__)
#app.config.from_object('wedding_site.app.config')

#if not app.debug:
if True:
    import logging

    file_handler = logging.FileHandler('/var/log/flask/weberror.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))


connection = happybase.Connection('cluster.davidbianco.net')


@app.route("/api/v1/info/song/<event>/<time>")
def get_song_info(event=False, time=False):
    pass

@app.route("/api/v1/info/artist/<event>/<time>")
def get_artist_info(event=False, time=False):
    pass

@app.route("/api/v1/info/users/demog/<gender>/<zipcode>/<age_bracket>")
def get_user_info_demog(event=False, time=False):
    pass

@app.route("/api/v1/info/users/<active_top>/<time>")
def get_user_info_counts(active_top=False, time=False):
    pass

@app.route("/")
def index():
    return render_template('reports.html')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Invalid API request."), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=DEBUG)


