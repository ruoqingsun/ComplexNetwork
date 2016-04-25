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
        if answer["Accepted"] == False:
            continue
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
        cn_mdb.answersGroup.insert({"acceptedAnswersGroup": answer_group})
    except Exception, e:
        print e


def exportAnswerGroup():
    collection = cn_mdb.answersGroup.find()
    answer_group = collection[1]["acceptedAnswersGroup"]
    print answer_group

    csvfile = open("answer_accepted_level.csv", "w")
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
