#-----------------------#
# musicbox.py           #
# David Bianco          #
# October 2014          #
#-----------------------#

import happybase

class User():
    active_listener_count = 0

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.user_id = ''
        self.gender = ''
        self.zipcode = ''

def settings():
    default = {}
    default['KAFKA_SERVER'] = 'cluster.davidbianco.net:8092'

    return default

def gen_event(event_json):
    #event_json: user_id, event_type, song_id, duration, ip, timestamp, text_message
    pass

def search(user_id, query_string, query_type):
    pass

def login(user_name,user_pass):
    pass

def register(new_user):
    pass

def logoff(user_id):
    pass

def test_listener():
    pass

if __name__ == '__main__':
    print "Running from the command line."

