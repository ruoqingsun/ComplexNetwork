import json
import pprint


# users = []
# with open('users.json') as user:
# 	for line in user:
# 		users.append(json.loads(line))
# print users[0]

questions = []
with open('questions.json') as question:
	for line in question:
		questions.append(json.loads(line))
# print questions[0]['answers'][0]['owner']['user_id']


question_owner = []
for each in questions:
    # pprint.pprint(each)
    try:
    	question_owner.append(each['owner']['user_id'])
    except Exception:
    	continue

answer_owner = []
for each in questions:
    # pprint.pprint(each)
    try:
    	for i in each['answers']:
    	    answer_owner.append(i['owner']['user_id'])
    except Exception:
    	continue


def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output

a = uniq(question_owner) + uniq(answer_owner)
b = uniq(a)


def find_question_id(input):
    output = []
    for x in input:
    	d = {}
    	d[x] = {}
        for y in questions:
            try:
                if x == y['owner']['user_id']:
    	            d[x]['question_date'] = y['creation_date']
    	        else:
    	        	for each in y['answers']:
    	        		if x == each['owner']['user_id']:
    	        			d[x]['answer_date'] = each['creation_date']
    	    except Exception:
    	    	continue
    	output.append(d)
    return output

c = find_question_id(b)
pprint.pprint(c)

with open('qustions_owner_id.json', 'w') as outfile:
    json.dump(c,outfile,indent=4)