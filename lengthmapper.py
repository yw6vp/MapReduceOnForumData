#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

next(reader, None)
for line in reader:
	if len(line) != 19:
		continue
	post_type = line[5]
	if post_type == 'question':
		print "{0}\tq{1}".format(line[0], len(line[4]))
	if post_type == 'answer':
		print "{0}\ta{1}".format(line[7], len(line[4]))
	