#!/usr/bin/python

import sys

toptags_question = []
toptags_all = []
last_tag = None
count_quesiton = 0
count_all = 0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue

	this_tag, this_type = data_mapped

	if not last_tag:
		last_tag = this_tag
	elif last_tag != this_tag:
		if len(toptags_question) < 10:
			toptags_question.append({last_tag: count_quesiton})
			toptags_question.sort(key = lambda x: x.values()[0], reverse = True)
		elif count_quesiton > toptags_question[9].values()[0]:
			toptags_question[9] = {last_tag: count_quesiton}
			toptags_question.sort(key = lambda x: x.values()[0], reverse = True)
		if len(toptags_all) < 10:
			toptags_all.append({last_tag: count_all})
			toptags_all.sort(key = lambda x: x.values()[0], reverse = True)
		elif count_all > toptags_all[9].values()[0]:
			toptags_all[9] = {last_tag: count_all}
			toptags_all.sort(key = lambda x: x.values()[0], reverse = True)
		count_quesiton = 0
		count_all = 0
		last_tag = this_tag
	count_all += 1
	if this_type == 'question':
		count_quesiton += 1

if last_tag:
	if len(toptags_question) < 10:
		toptags_question.append({last_tag: count_quesiton})
		toptags_question.sort(key = lambda x: x.values()[0], reverse = True)
	elif count_quesiton > toptags_question[9].values()[0]:
		toptags_question[9] = {last_tag: count_quesiton}
		toptags_question.sort(key = lambda x: x.values()[0], reverse = True)
	if len(toptags_all) < 10:
		toptags_all.append({last_tag: count_all})
		toptags_all.sort(key = lambda x: x.values()[0], reverse = True)
	elif count_all > toptags_all[9].values()[0]:
		toptags_all[9] = {last_tag: count_all}
		toptags_all.sort(key = lambda x: x.values()[0], reverse = True)

for pair in toptags_all:
	print "{0}\t{1}".format(pair.keys()[0], pair.values()[0])

for pair in toptags_question:
	print "{0}\t{1}".format(pair.keys()[0], pair.values()[0])

	