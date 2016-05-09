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


# print reputations[0]['level']

level = []
w = {}

for each in reputations:
    try:
        if each['level'] == 1:
            level.append(each['id'])
    except Exception:
        continue
w['level_5'] = level
# print w

return_questions = []
for each in level:
    try:
        for item in questions:
            if each == item['owner']['user_id']:
                return_questions.append(item)
    except Exception:
        continue
# print return_questions

question_date = []
first_answer_date = []
first_answer_accepted_date = []
time_interval_first = []
time_interval_accepted = []

for each in return_questions:
    try:
        question_date.append(each['creation_date'])
        first_answer_date.append(each['answers'][0]['creation_date'])
        a = (each['answers'][0]['creation_date'] - each['creation_date'])/(60*60)
        time_interval_first.append(a)
        # for i in each['answers']:
        #     try:
        #         if i['owner']['is_accepted'] == true:
        #             first_answer_accepted_date.append(i['creation_date'])
        #             b = (i['creation_date'] - each['creation_date'])/(60*60)
        #             time_interval_accepted.append(b)
        #     except Exception:
        #         continue

    except Exception:
        continue
# print time_interval

index = range(0,24)
number_first = []
number_accepted = []
for each in index:
    number_first.append(time_interval_first.count(each))
    # number_accepted.append(time_interval_accepted.count(each))
print number_first
print time_interval_first

with open('number_time_interval_1_min.csv', 'w') as outfile:
    json.dump(number_first,outfile,indent=4)