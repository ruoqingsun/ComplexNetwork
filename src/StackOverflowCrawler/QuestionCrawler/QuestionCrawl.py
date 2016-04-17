import stackexchange
import datetime
import calendar
from pymongo import MongoClient
import json
import pprint


API_KEY='JwPRMyfC9VTjKnaxe3h5Jg(('
MONGODB_URI = 'mongodb://localhost:27017/cn'

#Mongodb config

client = MongoClient(MONGODB_URI)
cn_mdb = client['cn']

#specify crawing data March 1st,2016

from_day = datetime.datetime(2016,3,1,0,0,0)
to_day = datetime.datetime(2016,3,1,23,59,59)
from_unixtime=calendar.timegm(from_day.timetuple())
to_unixtime=calendar.timegm(to_day.timetuple())

#get questions on March 1st, 2016
#get questions with tag 'python'
def questions():
    so = stackexchange.Site(stackexchange.StackOverflow, API_KEY)
    so.impose_throttling = True
    so.throttle_stop = False
    Questions = so.questions(tagged=['c++'], fromdate=from_unixtime,todate=to_unixtime,type=json).fetch()
    #pprint.pprint(dir(Questions))

    for each in Questions:
        #print dir(each)
        if '_params_' in each.json:
            del each.json['_params_']
        pprint.pprint(each.json)
        #questions={}
        #questions['']
        try:
            cn_mdb.cplusplus.insert_one(each.json)
        except Exception, e:
            print e
            continue

# Record Unique user Ids and save into Mongodb
def exportUserId():
    questions = cn_mdb.cplusplus.find()
    usersId = []
    num = 0;
    for question in questions:
        if question["owner"]["user_id"] not in usersId:
            usersId.append(question["owner"]["user_id"])
            #print("question["+str(num)+"]"+str(question["owner"]["user_id"]))

        if (question["answer_count"] > 0):
            for answer in question["answers"]:
                try:
                    answer["owner"]["user_id"]
                except Exception:
                    print "well, it WASN'T defined after all!"
                else:
                    if answer["owner"]["user_id"] not in usersId:
                        usersId.append(answer["owner"]["user_id"])
                        #print(answer["owner"]["user_id"])

        num=num+1

    try:
        cn_mdb.usersId.insert({"usersId": usersId})
    except Exception, e:
        print e

def users():
    collection = cn_mdb.usersId.find()
    usersId = collection[0]["usersId"]

    so = stackexchange.Site(stackexchange.StackOverflow, API_KEY)
    so.impose_throttling = True
    so.throttle_stop = False

    times = len(usersId)/100 + 1

    for time in range(0, times):

        id_list = "";
        for i in range(0, 100):
            if(100 * time + i >= len(usersId)):
                break
            if i==0:
                id_list = str(usersId[100 * time + i])
            else:
                id_list = id_list + ";" + str(usersId[100*time + i])

        Users = so.users(id_list)

        for each in Users:
            if '_params_' in each.json:
                del each.json['_params_']
            try:
                cn_mdb.users.insert_one(each.json)
                user = each.json
                cn_mdb.usersInfo.insert_one({
                    "id": user["user_id"],
                    "reputation": user["reputation"],
                    "badge_gold": user["badge_counts"]["gold"],
                    "badge_silver": user["badge_counts"]["silver"],
                    "badge_bronze": user["badge_counts"]["bronze"],
                })
            except Exception, e:
                print e
                continue

def edgesInfo():
    questions = cn_mdb.cplusplus.find()
    num = 0
    error = 0
    for question in questions:
        if (question["answer_count"] > 0):
            for answer in question["answers"]:
                try:
                    question["question_id"]
                    question["owner"]["user_id"]
                    answer["owner"]["user_id"]
                    answer["creation_date"]
                    answer["is_accepted"]
                except Exception:
                    print str(num)+": well, it WASN'T defined after all!"
                    error = error + 1
                else:
                    # print str(question["question_id"]) + " " + str(answer["creation_date"]) + " " + str(answer["creation_date"]-from_unixtime)
                    try:
                        cn_mdb.edgesInfo.insert({
                            "QId": question["question_id"],
                            "QerId": question["owner"]["user_id"],
                            "AerId": answer["owner"]["user_id"],
                            "ATime": (answer["creation_date"]-from_unixtime)/60/60/24,
                            "Accepted": answer["is_accepted"]
                        })
                    except Exception, e:
                        print e
        num = num + 1

    print num
    print error

#1. Crawl Questions (to be finished by Lu and Yiran)
#questions()

#2.Get all unique user ids and saves to collection "users"
#exportUserId()

#3. Extract user expertise information into collection "usersInfo"
#users()

#4. Extract graph edge for creating graph information into collectio200n "edgesInfo"
#edgesInfo()


