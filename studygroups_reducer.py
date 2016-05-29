#!/usr/bin/python

import sys

students = []
last_post = None

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	this_post, this_user = data

	if not last_post:
		last_post = this_post
	elif last_post != this_post:
		print "{0}\t{1}".format(last_post, students)
		last_post = this_post
		students = []
	students.append(int(this_user))

if last_post:
	print "{0}\t{1}".format(last_post, students)



	