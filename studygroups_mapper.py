#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

next(reader, None)
for line in reader:
	if len(line) != 19:
		continue
	node_type = line[5]
	author_id = line[3]
	if node_type == 'question':
		print "{0}\t{1}".format(line[0], author_id)
	else:
		print "{0}\t{1}".format(line[7], author_id)