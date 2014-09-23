#!/usr/bin/env python

import numpy
import h5py

tsv_file = "BGV4.tsv"
h5_file = "MillionSongSubset/data/B/G/V/TRBGVWB12903CE31A6.h5"

#numpy.savetxt(tsv_file, h5py.File(h5_file)['songs'], '%g', '\t')
numpy.savetxt(tsv_file, h5py.File("MillionSongSubset/data/B/G/V/TRBGVWB12903CE31A6.h5")['songs'], '%g', '\t')


