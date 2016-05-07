from pymongo import MongoClient
import datetime
import calendar
import json
import csv
import pprint


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

def questioner_group():
    questions = cn_mdb.questions.find()
    quers=[]
    quer_ques=[]
    for each_question in questions:
        temp={}
        #question
        try:
            qer = cn_mdb.userByReputation.find({ "id": each_question["owner"]["user_id"]})
            #print each_question["owner"]["user_id"]
            if each_question["owner"]["user_id"] not in quers:
                quers.append(each_question["owner"]["user_id"])
                temp['level'] = qer[0]["level"]
                temp['ques_count'] = 1
                quer_ques.append(temp)
            else:
                quer_find = quers.index(each_question["owner"]["user_id"])
                quer_ques[quer_find]['ques_count']+=1
        except Exception:
            continue
    # print quers
    # pprint.pprint(quer_ques)
    # print len(quers), len(quer_ques)
    cn_mdb.out_degree_group.insert(quer_ques)

def out_degree_group():
    ques_group = cn_mdb.out_degree_group.find()
    max_count = max([each["ques_count"] for each in ques_group])
    out_group=[[0 for x in range(max_count)] for y in range(5)]
    ques_group = cn_mdb.out_degree_group.find()
    for each in ques_group:
        out_group[each["level"]-1][each["ques_count"]-1]+=1
    print out_group
    out_total=[0 for x in range(5)]
    for x in range(len(out_total)):
        total=0
        for y in range(len(out_group[x])):
            total+=(out_group[x][y]*(y+1))
        out_total[x]=total
    print out_total
    csvfile = open("out_degree_group.csv", "w")
    csvfile1 = open("out_degree_total.csv","w")
    filednames = ["Newbie", "Learner", "User", "Professional", "Expert"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    writer1 = csv.DictWriter(csvfile1, fieldnames=filednames)
    writer1.writeheader()
    for x in range(max_count):
         writer.writerow({"Newbie": out_group[0][x], "Learner": out_group[1][x], "User": out_group[2][x], "Professional": out_group[3][x], "Expert": out_group[4][x]})
    csvfile.close()
    writer1.writerow({"Newbie": out_total[0], "Learner": out_total[1], "User": out_total[2], "Professional": out_total[3], "Expert": out_total[4]})
    csvfile1.close()

def answer_group():
    questions = cn_mdb.questions.find()
    aers=[]
    aer_answers=[]
    for each_question in questions:
        if each_question["answer_count"] >0:
            for each_answer in each_question["answers"]:
                temp={}
                try:
                    aer = cn_mdb.userByReputation.find({ "id": each_answer["owner"]["user_id"]})
                    print each_answer["owner"]["user_id"]
                    if each_answer["owner"]["user_id"] not in aers:
                        aers.append(each_answer["owner"]["user_id"])
                        temp['level'] = aer[0]["level"]
                        temp['ques_count'] = 1
                        aer_answers.append(temp)
                    else:
                        aer_find = aers.index(each_question["owner"]["user_id"])
                        aer_answers[aer_find]['ques_count']+=1
                except Exception:
                    continue
    print len(aers), len(aer_answers)
    cn_mdb.in_degree_group.insert(aer_answers)

def in_degree_group():
    answers_group = cn_mdb.in_degree_group.find()
    max_count = max([each["ques_count"] for each in answers_group])
    in_group=[[0 for x in range(max_count)] for y in range(5)]
    answers_group = cn_mdb.in_degree_group.find()
    for each in answers_group:
        in_group[each["level"]-1][each["ques_count"]-1]+=1
    print in_group
    in_total=[0 for x in range(5)]
    for x in range(len(in_total)):
        total=0
        for y in range(len(in_group[x])):
            total+=(in_group[x][y]*(y+1))
        in_total[x]=total
    print in_total
    csvfile = open("in_degree_group.csv", "w")
    csvfile1 = open("in_degree_total.csv","w")
    filednames = ["Newbie", "Learner", "User", "Professional", "Expert"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    writer1 = csv.DictWriter(csvfile1, fieldnames=filednames)
    writer1.writeheader()
    for x in range(max_count):
         writer.writerow({"Newbie": in_group[0][x], "Learner": in_group[1][x], "User": in_group[2][x], "Professional": in_group[3][x], "Expert": in_group[4][x]})
    csvfile.close()
    writer1.writerow({"Newbie": in_total[0], "Learner": in_total[1], "User": in_total[2], "Professional": in_total[3], "Expert": in_total[4]})
    csvfile1.close()
def in_out():
    edges = cn_mdb.edges_info.find()
    in_out_dis=[[0 for x in range(5)] for y in range(5)]
    for each in edges:
        print each['QerId'],each['AerId']
        try:
            qer = cn_mdb.userByReputation.find({ "id": each["QerId"]})
            aer = cn_mdb.userByReputation.find({ "id": each["AerId"]})
            print qer[0]['level'],aer[0]['level']
            in_out_dis[qer[0]["level"]-1][aer[0]["level"]-1]+=1
        except Exception:
            continue
    print in_out_dis
    csvfile = open("in_out.csv", "w")
    filednames = ["Newbie", "Learner", "User", "Professional", "Expert"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for x in range(len(in_out_dis)):
        writer.writerow({"Newbie": in_out_dis[x][0], "Learner": in_out_dis[x][1], "User": in_out_dis[x][2], "Professional": in_out_dis[x][3], "Expert": in_out_dis[x][4]})
    csvfile.close()

def first_day():
    questions = cn_mdb.questions.find()
    ques_min = [ 0 for x in range(24*60)]
    for each_ques in questions:
        minute = (each_ques['creation_date'] - from_unixtime)/60
        ques_min[minute]+=1
    print ques_min
    csvfile = open("ques_min.csv", "w")
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
    writer.writerow(ques_min)

#answerInterval()
#answer_count()
#st_answer()
#answerIntervalst()
#accept_answer_st()
#questioner_group()
#out_degree_group()
#answer_group()
#in_degree_group()
#in_out()
first_day()