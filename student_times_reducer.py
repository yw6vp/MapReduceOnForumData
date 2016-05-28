#!/usr/bin/python

import sys

last_user = None
freq = [0 for i in range(24)]

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	user_id, hour = data
	if not last_user:
		last_user = user_id
	elif last_user != user_id:
		max_freq = max(freq)
		for i in range(24):
			if freq[i] == max_freq:
				print "{0}\t{1}".format(last_user, i)
		freq = [0 for i in range(24)]
		last_user = user_id
	freq[int(hour)] += 1

if last_user:
	max_freq = max(freq)
	print "{0}\t{1}".format(last_user, freq.index(max_freq))