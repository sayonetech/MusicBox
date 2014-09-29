import subprocess
import happybase
import sys
import random

connection = happybase.Connection('cluster.davidbianco.net')

def generator(start_userid, num):
    limit = sys.argv[1] or 10
    user_ids = []
    table = connection.table('user_info')

    for key, data in table.scan(row_start=start_userid, limit=num):
        user_ids.append(key)

    for user_id in user_ids:
        subprocess.popen('event_gen_worker.py',user_id)

    return start_userid

# get list of active users and frequency from database
# choose active listener
# user login every X minutes, spawn child process
# generate new user every X minutes
# deactivate user every 1 hour ?

def random_wait():
    wait_mins = (0, 43, 65, 244, 245, 246, 247, 422, 424, 425, 428, 600)
    wait_next = random.choice(wait_mins)
    return wait_next


if (__name__ == "__main__"):
    num = sys.argv[1] or 10
    start_userid = '0003df7f-d6a7-4298-8260-e09c8167f74e'
    while True:
        next_userid = generator(start_userid, num)
        sleep(random_wait())
        start_userid = next_userid
        num = random.choice([1, 2, 4, 8, 16, 32, 64,]) # 128, 256, 512, 1024

def generate_event():
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


