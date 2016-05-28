#!/usr/bin/python

import sys

last_id = None
total_length = 0
questin_length = 0
count = 0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue

	this_id, this_value = data_mapped
	post_type = this_value[0]
	this_length = this_value[1:]
	if not last_id:
		last_id = this_id
	elif last_id != this_id:
		mean_answer_length = float(total_length) / count if count > 0 else 0
		print "{0}\t{1}\t{2}".format(last_id, questin_length, mean_answer_length)
		last_id = this_id
		count = 0
		total_length = 0
		questin_length = 0
	if post_type == 'a':
		count += 1
		total_length += int(this_length)
	else:
		questin_length = int(this_length)

if last_id:
	mean_answer_length = float(total_length) / count if count > 0 else 0
	print "{0}\t{1}\t{2}".format(last_id, questin_length, mean_answer_length)


