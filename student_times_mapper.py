#!/usr/bin/python

from datetime import datetime
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

next(reader, None)
for line in reader:
	if len(line) != 19:
		continue
	user_id = line[3]
	time = line[8]
	index = time.find('+')
	if index >= 0:
		time = time[:index]
	hour = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').hour
	print "{0}\t{1}".format(user_id, hour)