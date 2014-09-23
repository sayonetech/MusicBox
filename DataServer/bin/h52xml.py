#!/usr/bin/env python

import glob
import os

outdir = "xml/"

# h5dump -x MillionSongSubset/data/B/G/V/TRBGVWB12903CE31A6.h5 > BGV4.xml
# MillionSongSubset-data-B-G-V-TRBGVWB12903CE31A6.h5.touch
files = glob.glob('MillionSongSubset/data/B/*/*/*.h5')
x = 0

for infile in files:
    x += 1
    outfile = outdir + "B" + str(x) + ".xml"
    cmd = "h5dump -x %s > %s" % (infile, outfile)
    os.system(cmd)
    #os.system("h5dump -x MillionSongSubset/data/B/G/V/TRBGVWB12903CE31A6.h5 > BGV4.xml")
    #print file



