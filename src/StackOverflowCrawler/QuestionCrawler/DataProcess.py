from pymongo import MongoClient
import datetime
import calendar
import json


API_KEY='JwPRMyfC9VTjKnaxe3h5Jg(('
MONGODB_URI = 'mongodb://localhost:27017/cn'

#Mongodb config

client = MongoClient(MONGODB_URI)
cn_mdb = client['cn']

#Question creation data March 1st

from_day = datetime.datetime(2016,3,1,0,0,0)
to_day = datetime.datetime(2016,3,1,23,59,59)
from_unixtime=calendar.timegm(from_day.timetuple())
to_unixtime=calendar.timegm(to_day.timetuple())

def answerInterval():
    questions = cn_mdb.questionsId.find()
    all_interval=[]
    for question_id in questions[0]["quesitonsId"]:
        answer_interval = []
        answer_time=[]
        answers = cn_mdb.edges_info.find({"QId":question_id})
        last_time = 0
        for each_answer in answers:
            answer_time.append(each_answer["ATime"])
        if answer_time:
            for each_time in sorted(answer_time):
                interval=each_time-last_time
                all_interval.append(interval)
                last_time=each_time
                answer_interval.append(interval)
            temp={}
            temp["QId"]=question_id
            temp["intervals"]=answer_interval
            cn_mdb.answerIntervals.insert_one(temp)
            #print answer_interval
    cn_mdb.allAnswerIntervals.insert({"timeInterval": all_interval})

def answer_count():
    questions = cn_mdb.questions.find()
    output=[]
    jsonfile = open('answer_count.js', 'w')
    for each_ques in questions:
        temp={}
        temp["question_id"]=each_ques["question_id"]
        temp["answer_count"]=each_ques["answer_count"]
        output.append(temp)
    json.dump(output,jsonfile,indent=4)
    jsonfile.close()

answer_count()




#answerInterval()