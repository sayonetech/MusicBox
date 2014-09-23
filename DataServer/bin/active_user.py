#!/usr/bin/env python

import random
import time
import sys

user_id = sys.argv(0)
song_id = sys.argv(1)

sleep_mins = (43, 65, 244, 245, 246, 247, 422, 424, 425, 428, 600)
user_action = ('pause', 'skip', 'thumbs-up', 'thumbs-dn')

while(True):
	action = random.choice(user_action)
	if action == 'pause':
		# set pause condition
		time.sleep(42)
		# set play condition
	elif action == 'skip':
		# choose or play next song
	elif action == 'thumbs-up':
		# record user pref
	elif action == 'thumbs-dn':
		# record user pref
		req_url = 'user/%s/song/%s/thumbs-down' % (user_id, song_id)
		

	
	choice = random.choice(sleep_mins)
	choice = choice / 10
	print "Sleeping for %s seconds..." % choice
	time.sleep(choice)


