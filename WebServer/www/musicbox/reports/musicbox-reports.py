from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify
import happybase
import json


DEBUG = True
SECRET_KEY = 'fjl3lf4846kl43#(p'
SERVER_NAME = 'davidbianco.net'

app = Flask(__name__)
app.debug = True

#if not app.debug:
if True:
    import logging

    file_handler = logging.FileHandler('/var/log/flask/musicbox-reports/weberror.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))

oauth_consumer_key = '7d5kwsncn39p'
oauth_consumer_secret = 'at728qxu6zkusyh4'

connection = happybase.Connection('cluster.davidbianco.net')

@app.route('/playlist-test/<track_id>')
def generate_playlist(track_id):
    table = connection.table('song_info_20cols')
    table2 = connection.table('artist_info_20cols')
    html = "\n<table>\n<tr><th>Artist</th><th>Album</th><th>Song</th><th>Duration</th></tr>\n"
    for i in range(10):
        row = table.row(track_id)
        sim_artists = row['info:similar_artists'].split(',')
        html += row['info:similar_artists']
        html += "<tr><td>" + row['info:artist_name'] + "</td><td>" + row['info:release'] + "</td>"
        html += "<td>" + row['info:title'] + "</td><td>" + sim_artists[0] + "</td></tr>\n"

        sim_artists = row['info:similar_artists'].split(',')
        no_record = True
        while no_record:
            for sim_artist in sim_artists:
                row2 = table2.row(sim_artist)
                html += row2

                if row2:
                    track_id = row2['info:track_id']
                    no_record = False

            html += "no artist found"
            no_record = False

    html += "\n</table>\n"

    return render_template('playlist.html', html=html)


@app.route('/search', methods=['GET', 'POST'])
def search():
    # artist image http://api.7digital.com/1.2/artist/details?artistId=1&imageSize=200&oauth_consumer_key=7d5kwsncn39p
    # song preview http://previews.7digital.com/clip/4308713?oauth_consumer_key=7d5kwsncn39p&country=US
    pass

@app.route('/search/song/<song>')
def search_song(song=False):
    table = connection.table('song_search')
    print table
    if song:
        #row = table.row(song)
        song = song + '::'
        rows = table.scan(row_prefix=song)
        print rows
        if not rows:
            datas['error'] = "Song not found"
            datas['query'] = song
        for key, data in rows:
            datas = data
    else:
        datas['error'] = "Invalid search request"

    return jsonify(**datas)

@app.route('/api/v1/info/song/<event>/<time>')
def get_song_info(event=False, time=False):
    table = connection.table('song_search')
    row = table.row(song)

@app.route('/api/v1/info/artist/<event>/<time>')
def get_artist_info(event=False, time=False):
    pass

@app.route('/api/v1/info/users/demog/<gender>/<zipcode>/<age_bracket>')
def get_user_info_demog(event=False, time=False):
    pass

@app.route('/api/v1/info/users/<active_top>/<time>')
def get_user_info_counts(active_top=False, time=False):
    pass

@app.route('/')
def index():
    return render_template('reports.html')

@app.route('/api/v1/doc')
def doc():
    return render_template('doc.html')

@app.route('/github')
def github():
    return render_template('github.html')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Invalid API request.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=DEBUG)


