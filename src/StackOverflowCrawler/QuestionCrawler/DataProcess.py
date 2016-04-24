from pymongo import MongoClient
import datetime
import calendar
import json
import csv


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
    jsonfile = open('answer_count.json', 'w')
    for each_ques in questions:
        temp={}
        temp["question_id"]=each_ques["question_id"]
        temp["answer_count"]=each_ques["answer_count"]
        output.append(temp)
    json.dump(output,jsonfile,indent=4)
    jsonfile.close()

# answer distribution
def st_answer():
    jsonfile = open('answer_count.json','r')
    data = json.load(jsonfile)
    counts = [each["answer_count"] for each in data]
    uni_counts = list(set(counts))
    counts_st = []
    for x in range(14):
        counts_st.append(0)
    print counts_st
    for each in data:
        counts_st[each["answer_count"]]+=1
    print counts_st
    csvfile=open("answer_statistic.csv","w")
    fieldnames = ['answer_counts', 'num']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(14):
        writer.writerow({"answer_counts":x, "num":counts_st[x]})
    csvfile.close()

#answer intervals distribution
def answerIntervalst():
    intervals = cn_mdb.allAnswerIntervals.find()
    all_intervals = list(set(intervals[0]['timeInterval']))
    interval_st=[0]*31
    for each in intervals[0]['timeInterval']:
        if each <=30:
            interval_st[each]+=1
    print interval_st
    csvfile = open("answer_intervals_statistic.csv","w")
    filednames=["day","num"]
    writer=csv.DictWriter(csvfile,fieldnames=filednames)
    writer.writeheader()
    for x in range(31):
        writer.writerow({"day":all_intervals[x],"num":interval_st[x]})
    csvfile.close()

def accept_answer_st():
    answers = cn_mdb.edges_info.find()
    accpet_answers = [each for each in answers if each['Accepted']==True]
    accept_time = list(set([each['ATime'] for each in accpet_answers]))
    #print accept_time
    accept_time_st=[0]* (max(accept_time)+1)
    for each in accpet_answers:
        accept_time_st[each['ATime']]+=1
    #print accept_time_st
    csvfile = open("accpet_answer_time_st.csv","w")
    filednames=["day","num"]
    writer=csv.DictWriter(csvfile,fieldnames=filednames)
    writer.writeheader()
    for x in range(len(accpet_answers)):
        writer.writerow({"day":x,"num":accept_time_st[x]})
    csvfile.close()


#answerInterval()
#answer_count()
#st_answer()
#answerIntervalst()
accept_answer_st()