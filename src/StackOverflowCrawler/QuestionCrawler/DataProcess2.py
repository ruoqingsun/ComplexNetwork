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

def answerGroup():
    answers = cn_mdb.edgesInfo.find()
    answer_group = [[0 for x in range(5)] for y in range(5)]
    for answer in answers:
        qer = cn_mdb.usersInfo.find({ "id":  answer["QerId"]})
        aer = cn_mdb.usersInfo.find({ "id":  answer["AerId"]})
        try:
            qer[0]["level"] - 1
            aer[0]["level"] - 1
        except Exception:
            print "well, questioner's id WASN'T defined after all!"
        else:
            answer_group[qer[0]["level"]-1][aer[0]["level"]-1] += 1
            # csvfile = open("accpet_answer_time_st.csv","w")


    try:
        cn_mdb.answersGroup.insert({"answersGroup": answer_group})
    except Exception, e:
        print e
    # csvfile = open("answer_level.csv", "w")
    # filednames = ["Newbie", "Learner", "User", "Professional", "Expert"]
    # writer = csv.DictWriter(csvfile, fieldnames=filednames)
    # writer.writeheader()
    # for x in range(len(accept_time_st)):
    #     writer.writerow({"Newbie": x[0], "Learner": x[1], "User": x[2], "Professional": x[3], "Expert": x[4]})
    # csvfile.close()
    # print answer_group

    # print answers
    # accpet_answers = [each for each in answers if each['Accepted']==True]
    # accept_time = list(set([each['ATime'] for each in accpet_answers]))
    # print accept_time
    # accept_time_st=[0]* (max(accept_time)+1)
    # for each in accpet_answers:
    #     accept_time_st[each['ATime']]+=1
    # #print accept_time_st
    # csvfile = open("accpet_answer_time_st.csv","w")
    # filednames=["day","num"]
    # writer=csv.DictWriter(csvfile,fieldnames=filednames)
    # writer.writeheader()
    # for x in range(len(accept_time_st)):
    #     writer.writerow({"day":x,"num":accept_time_st[x]})
    # csvfile.close()

def exportAnswerGroup():
    collection = cn_mdb.answersGroup.find()
    answer_group = collection[0]["answersGroup"]
    print answer_group

    csvfile = open("answer_level.csv", "w")
    filednames = ["Newbie", "Learner", "User", "Professional", "Expert"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for x in range(len(answer_group)):
        writer.writerow({"Newbie": answer_group[x][0], "Learner": answer_group[x][1], "User": answer_group[x][2], "Professional": answer_group[x][3], "Expert": answer_group[x][4]})
    csvfile.close()

    # for x in range(len(answer_group)):
    #     print answer_group[x][1]

#answerGroup()
exportAnswerGroup()
