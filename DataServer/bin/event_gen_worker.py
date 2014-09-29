#!/usr/bin/env python

# event_gen_worker.py
# David Bianco - Sept. 2014

from faker import Factory
import random
import sys
import requests
import urllib
from datetime import timedelta, datetime

def new_user(id=0):

    a = 1
    if id % 100 == 0:
        a = 0

    userid = uuid.uuid4()
    fname = fake.first_name()
    lname = fake.last_name()
    email = fake.safe_email()

    choice_list = ['1'] * 10 + ['2'] * 20 + ['3'] * 35 + ['4'] * 25 + ['5'] * 10
    freq_wt = random.choice(choice_list)

    d1 = datetime.strptime('2010', '%Y')
    d2 = datetime.strptime('8/18/2014', '%m/%d/%Y')
    d3 = random_date(d1, d2)
    acct_created = d3
    #acct_created = fake.iso8601()

    d4 = datetime.strptime('9/18/2014', '%m/%d/%Y')
    last_login = random_date(d3, d4)
    #last_login = fake.iso8601()

    zipcode = fake.zipcode()

    y1 = datetime.strptime('1930', '%Y')
    y2 = datetime.strptime('2000', '%Y')
    birth_year = datetime.strftime(random_date(y1, y2), '%Y')
    #birth_year = fake.year()

    gender = random.choice(["M", "F"])
    active = a
    ip_addr = fake.ipv4()
    #my_stations =
    #similar_users =

    with open('../data/user_init.csv', 'a') as u_csvfile:
        print >> u_csvfile, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (userid,fname,lname,email,freq_wt,acct_created,last_login,zipcode,birth_year,gender,active,ip_addr)

    return userid, acct_created, last_login, active


def random_wait():
    wait_seconds = (43, 65, 244, 245, 246, 247, 422, 424, 425, 428, 600)
    wait_next = random.choice(wait_seconds)
    return wait_next


def new_event(user_id):
    #next_event = 'login'
    #choice_list = ['search'] * 28 + ['play'] * 68 + ['exit'] * 4
    #event_choice = random.choice(choice_list)
#select active user (uid,begindate,lastdate,ip)
#select first song in hotttnesss range (sid,sim_artists) [9] * 50 + [8] * 30 + [7] * 15 + [5] * 5
#login user
# LOOP: freq_wt ^ (freq-1, freq) or 1 if <0
    next_event = 'login'
    user_is_active = True
    #ip4 = fake.ipv4()

    while user_is_active:
        d = {}
        d['ip4'] = ip4
        url = 'http://insight.davidbianco.net/user/' + user_id + '/' + event
        if next_event == 'login':
            r = requests.get(url)
            choice_list = ['search'] * 28 + ['play'] * 68 + ['exit'] * 4
            next_event = random.choice(choice_list)
        elif next_event == 'search':
            search_query = 'love'
            search_query = urllib.quote_plus(search_query)
            url += '/song/' + search_query
            d['query'] = search_query
            #d['query'] = fake.words().join()
            choice_list = ['play'] * 70 + ['exit'] * 5 + ['search'] * 25
            new_time = last_time + timedelta(seconds=random_wait())
            d['timestamp'] = datetime.strftime(new_time, '%c')
            last_time = new_time
            next_event = random.choice(choice_list)
        elif next_event == 'play':
            url += '/song/' + song_id
            sid = fake.md5()
            d['songid'] = sid
            new_time = last_time + timedelta(seconds=random_wait())
            d['timestamp'] = datetime.strftime(new_time, '%c')
            last_time = new_time
            choice_list = ['tup'] * 30 + ['tdn'] * 30 + ['exit'] * 5 + ['pause'] * 5 + ['skip'] * 5 + ['play'] * 25
            next_event = random.choice(choice_list)
        elif next_event == 'exit':
            new_time = last_time + timedelta(seconds=random_wait())
            d['timestamp'] = datetime.strftime(new_time, '%c')
            last_time = new_time
            next_event = 'login'
            ip4 = fake.ipv4()
            user_is_active = False
        else:
            # tup, tdn, pause, skip
            url += '/song/' + song_id
            d['songid'] = sid
            next_event = next_event
            new_time = last_time + timedelta(seconds=random_wait())
            d['timestamp'] = datetime.strftime(new_time, '%c')
            last_time = new_time
            choice_list = ['search'] * 28 + ['play'] * 68 + ['exit'] * 4
            next_event = random.choice(choice_list)

        json.dumps(d)
        with open('user_events_init_pretty.json', 'a') as prettyfile:
            res = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
            prettyfile.write(res)
            #json.dump(d, prettyfile
        with open('user_events_init.json', 'a') as outfile:
            json.dump(d, outfile)

if (__name__ == "__main__"):
    user_id = sys.argv[1]

    while True:
        new_event(user_id)



                #json.dumps(d)

                #print "%s,login,%s" % (uid,login_date)
                #wait_next = random_wait
                #new_time = login_date + random_wait()
                #next_event = event_choice
                #d['timestamp'] = login_date + random_wait()
                #json.dumps(d)


                #print "%s,%s,%s" % (uid, event_choice, new_time, query)
#login btwn begin-last date
#play or search and play
#tup,tdn,skip,pause
#exit

#userid,begindate,lastdate,
# tup,tdn,pause,skip,login,search,play
# userid,event,timestamp,songid


