import json
import pprint

questions = []
with open('questions.json') as question:
	for line in question:
		questions.append(json.loads(line))

reputations = []

with open('usersInfoByReputation.json') as reputation:
	for line in reputation:
		reputations.append(json.loads(line))



level = []
w = {}
for each in reputations:
    try:
        if each['level'] == 5:
            level.append(each['id'])
    except Exception:
        continue
# w['level_1'] = level


return_questions = []
for each in level:
    try:
        for item in questions:
            if each == item['owner']['user_id']:
                return_questions.append(item)
    except Exception:
        continue
print len(return_questions)

Q_A1_time_interval = []
for each in return_questions:
    try:
        for i in each['answers']:
            try:
            	# print i
                if i['is_accepted'] == True:
                    a = i['creation_date'] - each['creation_date']
                    Q_A1_time_interval.append(a)
            except Exception:
                continue
    except Exception:
        continue

print len(Q_A1_time_interval)
print Q_A1_time_interval

hours = []
for each in Q_A1_time_interval:
	hours.append(each/3600)
print hours

count_accepted = []
for i in range(0,23):
	count_accepted.append(hours.count(i))

print count_accepted

with open('accepted_time_interval_5_hour.csv', 'w') as outfile:
    json.dump(count_accepted,outfile,indent=4)





# view_counts = []
# for each in return_questions:
# 	view_counts.append(each['view_count'])
# # print view_counts

# average = sum(view_counts)/len(return_questions)
# print average


