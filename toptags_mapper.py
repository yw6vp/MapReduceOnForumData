#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

next(reader, None)
for line in reader:
	if len(line) != 19:
		continue
	tags = line[2].split(' ')
	for tag in tags:
		if tag.strip():
			print "{0}\t{1}".format(tag, line[5].strip())