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

def questions():
    so = stackexchange.Site(stackexchange.StackOverflow, API_KEY)
    so.impose_throttling = True
    so.throttle_stop = False
    Questions = so.questions(fromdate=from_unixtime,todate=to_unixtime,type=json).fetch()
    #pprint.pprint(dir(Questions))

    for each in Questions:
        #print dir(each)
        if '_params_' in each.json:
            del each.json['_params_']
        pprint.pprint(each.json)
        #questions={}
        #questions['']
        try:
            cn_mdb.question.insert_one(each.json)
        except Exception, e:
            print e
            continue


questions()



