#!/usr/bin/env python

import os
from xml.dom import minidom

xmlfile = os.environ['HOME'] + '/data/tbdmsd-aws-bucketlist.xml'

xmldoc = minidom.parse(xmlfile)

keylist = xmldoc.getElementsByTagName('Key')

for keys in keylist:
	key = keys.childNodes[0].nodeValue
	#print 'wget -P ~/msd -a ~/msd/0msd_extract.log http://tbmmsd.s3.amazonaws.com/%s' % key
	print 'http://tbmmsd.s3.amazonaws.com/%s' % key


