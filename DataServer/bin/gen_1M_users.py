from faker import Factory
import random
import uuid
import json
from datetime import timedelta, datetime

fake = Factory.create()


def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def new_user(id=0):

    a = 1
    if id % 100 == 0:
        a = 0

    userid = uuid.uuid4()
    fname = fake.first_name()
    lname = fake.last_name()
    email = fake.safe_email()

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

    with open('user_init.csv', 'a') as u_csvfile:
        print >> u_csvfile, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (userid,fname,lname,email,acct_created,last_login,zipcode,birth_year,gender,active,ip_addr)

    return userid, acct_created, last_login, active

def random_wait():
    wait_mins = (43, 65, 244, 245, 246, 247, 422, 424, 425, 428, 600)
    wait_next = random.choice(wait_mins)
    return wait_next


if (__name__ == "__main__"):
    num_users = 10
    choice_list = 40
    #choice_list = ['4'] * 5 + ['40'] * 15 + ['120'] * 30 + ['240'] * 30 + ['400'] * 20
    num_events_per_user = int(random.choice(choice_list))
    for i in range(num_users):
        #u = new_user(i)
        (uid,begindate,lastdate,active) = new_user(i)
        #print u
        if active:
            #d['event'] = 'login'
            #choice_list = ['search'] * 28 + ['play'] * 68 + ['exit'] * 4
            #event_choice = random.choice(choice_list)
            next_event = 'login'
            ip4 = fake.ipv4()

            for j in range(num_events_per_user):
                if j == num_events_per_user - 1:
                    if d['event'] == 'exit':
                        continue
                    else:
                        next_event = 'exit'
                d = {}
                d['uid'] = str(uid)
                d['ip4'] = ip4
                d['event'] = next_event
                if d['event'] == 'login':
                    login_date = random_date(begindate, lastdate)
                    new_time = login_date
                    d['timestamp'] = datetime.strftime(new_time, '%c')
                    last_time = new_time
                    choice_list = ['search'] * 28 + ['play'] * 68 + ['exit'] * 4
                    next_event = random.choice(choice_list)
                elif d['event'] == 'search':
                    phrase = ' '.join(fake.words())
                    d['query'] = phrase
                    #d['query'] = fake.words().join()
                    choice_list = ['play'] * 70 + ['exit'] * 5 + ['search'] * 25
                    new_time = last_time + timedelta(seconds=random_wait())
                    d['timestamp'] = datetime.strftime(new_time, '%c')
                    last_time = new_time
                    next_event = random.choice(choice_list)
                elif d['event'] == 'play':
                    sid = fake.md5()
                    d['songid'] = sid
                    new_time = last_time + timedelta(seconds=random_wait())
                    d['timestamp'] = datetime.strftime(new_time, '%c')
                    last_time = new_time
                    choice_list = ['tup'] * 30 + ['tdn'] * 30 + ['exit'] * 5 + ['pause'] * 5 + ['skip'] * 5 + ['play'] * 25
                    next_event = random.choice(choice_list)
                elif d['event'] == 'exit':
                    new_time = last_time + timedelta(seconds=random_wait())
                    d['timestamp'] = datetime.strftime(new_time, '%c')
                    last_time = new_time
                    next_event = 'login'
                    ip4 = fake.ipv4()
                else:
                    d['songid'] = sid
                    d['event'] = next_event
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

                #json.dumps(d)

                #print "%s,login,%s" % (uid,login_date)
                #wait_next = random_wait
                #new_time = login_date + random_wait()
                #d['event'] = event_choice
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


