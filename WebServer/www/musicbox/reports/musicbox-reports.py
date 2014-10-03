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

    file_handler = logging.FileHandler('./weberror.log')
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
    row2 = {}
    html = "\n<table>\n<tr><th>Artist</th><th>Album</th><th>Song</th><th>Duration</th></tr>\n"
    for i in range(10):
        row = table.row(track_id)
        sim_artists = row['info:similar_artists'].split(',')
        #html += row['info:similar_artists']
        #html += "<tr><td>" + row['info:artist_name'] + "</td><td>" + row['info:release'] + "</td>"
        #html += "<td>" + row['info:title'] + "</td><td>" + sim_artists[0] + "</td></tr>\n"

        sim_artists = row['info:similar_artists'].split(',')
        #html += str(sim_artists)
        no_record = True
        while no_record:
            for sim_artist in sim_artists:
                html += sim_artist + "\n"
                #row2 = table2.row(sim_artist)
                row2 = False
                html += "\n" + str(row2)

                if row2:
                    track_id = row2['info:track_id']
                    no_record = False

            html += "no artist found"
            no_record = False

    html += "\n</table>\n"

    return render_template('playlist.html', html=html, data=data)


    # artist image http://api.7digital.com/1.2/artist/details?artistId=1&imageSize=200&oauth_consumer_key=7d5kwsncn39p
    # song preview http://previews.7digital.com/clip/4308713?oauth_consumer_key=7d5kwsncn39p&country=US

@app.route('/search', methods=['GET', 'POST'])
#@app.route('/search/<q_type>/<q_string>')
#def search_song(q_type=False, q_string=False):
def search():
    datas = {}

    if method == 'POST':
        song_table = connection.table('song_search')
        artist_table = connection.table('artist_search')
        if q_type == 'song':
            song = q_string + '::'
            rows = song_table.scan(row_prefix=song)
            print rows
            if not rows:
                datas['error'] = "Song not found"
                datas['query'] = song
            else:
                for key, data in rows:
                    datas = data
        elif q_type == 'artist':
            artist = q_string + '::'
            rows = artist_table.scan(row_prefix=artist)
            print rows
            if not rows:
                datas['error'] = "Arist not found"
                datas['query'] = q_string
            else:
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
    data = {}
    data['plays'] = []
    data['skip'] = []
    data['tup'] = []
    data['tdn'] = []
    table = connection.table('event_log_artists')
    data['search_type'] = 'Artist'
    data['search_result'] = 'Alicia Keys'

    #id = request.form.id
    #begin_date = request.form.begin_date
    #end_date = request.form.end_date
    #begin_range = id + '_' + begin_date
    #end_range = id + '_' + end_date
    begin_range = ' AR52EZT1187B9900BF_20130101'
    #end_range = ' AR52EZT1187B9900BF_20130613'
    end_range = ' AR52EZT1187B9900BF_20131230'

    for rowkey, rowdata in table.scan(row_start=begin_range, row_stop=end_range):
        data['plays'].append(int(rowdata['info:play_count']))
        data['skip'].append(int(rowdata['info:skip']))
        data['tup'].append(int(rowdata['info:tup_count']))
        data['tdn'].append(int(rowdata['info:tdn_count']))

    return render_template('reports.html', data=data)

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


