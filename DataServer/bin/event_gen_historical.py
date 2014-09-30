#!/usr/bin/env python

import random
from datetime import datetime, timedelta


def aggregate_day():
    #filename = '../data/top100songs.txt'
    filename = '../data/top100artists.txt'
    with open(filename, 'r') as f:
        for line in f:
            counter = 0
            date = datetime.strptime('20120101', '%Y%m%d')
            songart_id = line.rstrip('\n')
            while counter < 865:
                date_str = datetime.strftime(date, '%Y%m%d')
                counter += 1
                play_count = random.randint(20,150)
                tup_count = random.randint(0,play_count-5)
                tdn_count = random.randint(0,play_count-tup_count)
                skip_count = random.randint(0,play_count-(tup_count+tdn_count))
                d = songart_id + '_' + date_str
                d += "\t" + songart_id
                d += "\t" + date_str
                d += "\t" + str(play_count)
                d += "\t" + str(tup_count)
                d += "\t" + str(tdn_count)
                d += "\t" + str(skip_count)
                print d
                date = date + timedelta(days=1)

if (__name__ == "__main__"):
    aggregate_day()


