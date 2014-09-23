#!/usr/bin/env python

attrs = ['track-id'
,'analysis-sample-rate'
,'artist-7digitalid'
,'artist-familiarity'
,'artist-hotttnesss'
,'artist-id'
,'artist-latitude'
,'artist-location'
,'artist-longitude'
,'artist-mbid'
,'artist-mbtags'
,'artist-mbtags-count'
,'artist-name'
,'artist-playmeid'
,'artist-terms'
,'artist-terms-freq'
,'artist-terms-weight'
,'audio-md5'
,'bars-confidence'
,'bars-start'
,'beats-confidence'
,'beats-start'
,'danceability'
,'duration'
,'end-of-fade-in'
,'energy'
,'key'
,'key-confidence'
,'loudness'
,'mode'
,'mode-confidence'
,'release'
,'release-7digitalid'
,'sections-confidence'
,'sections-start'
,'segments-confidence'
,'segments-loudness-max'
,'segments-loudness-max-time'
,'segments-loudness-max-start'
,'segments-pitches'
,'segments-start'
,'segments-timbre'
,'similar-artists'
,'song-hotttnesss'
,'song-id'
,'start-of-fade-out'
,'tatums-confidence'
,'tatums-start'
,'tempo'
,'time-signature'
,'time-signature-confidence'
,'title'
,'track-7digitalid'
,'year'
]

import csv

tsvfile = "A2.tsv"
i = 0

with open(tsvfile) as tsv:
    for line in csv.reader(tsv, delimiter='\t'):
	    for item in line:
	        i += 1
		attr = attrs.pop(0)
		#print "%d - %s: %s" % (i,attr, str(item))
		print ",%s" % attr
    	    break


