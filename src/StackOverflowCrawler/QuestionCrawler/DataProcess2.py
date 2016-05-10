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

def exportEdgeInfo():
    collection = cn_mdb.edgesInfo.find()
    edges = [];
    edges_innode = []
    edges_outnode = []
    weights = [];
    csvfile = open("digraph_edges.csv", "w")
    filednames = ["In", "Out", "Weight"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for edge in collection:
        temp = str(edge["QerId"])+str(edge["AerId"])
        if temp in edges:
            weights[edges.index(temp)] = weights[edges.index(temp)] + 1
            print edges.index(temp)
        else:
            edges.append(temp)
            edges_innode.append(edge["QerId"])
            edges_outnode.append(edge["AerId"])
            weights.append(1)

    for i in range(len(edges)):
        writer.writerow({"In": edges_innode[i], "Out": edges_outnode[i], "Weight": weights[i]})

    csvfile.close()

def exportNodeWeights():
    collection = cn_mdb.edgesInfo.find();
    nodes = [];
    nodes_in = [];
    nodes_out = [];
    csvfile = open("digraph_nodes_weights.csv", "w")
    filednames = ["Node", "In_weight", "Out_weight"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for edge in collection:
        if edge["QerId"] in nodes:
            nodes_out[nodes.index(edge["QerId"])] = nodes_out[nodes.index(edge["QerId"])] + 1
        else:
            nodes.append(edge["QerId"])
            nodes_in.append(0)
            nodes_out.append(1)

        if edge["AerId"] in nodes:
            nodes_in[nodes.index(edge["AerId"])] = nodes_in[nodes.index(edge["AerId"])] + 1
        else:
            nodes.append(edge["AerId"])
            nodes_in.append(1)
            nodes_out.append(0)


    for i in range(len(nodes)):
        writer.writerow({"Node": nodes[i], "In_weight": nodes_in[i], "Out_weight": nodes_out[i]})
    csvfile.close()

def exportNodeWeightsSize():
    collection = cn_mdb.edgesInfo.find();
    nodes = [];
    nodes_in = [];
    nodes_out = [];
    csvfile = open("digraph_weights_combination.csv", "w")
    filednames = ["In-degree", "Out-degree", "Weight"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for edge in collection:
        if edge["QerId"] in nodes:
            nodes_out[nodes.index(edge["QerId"])] = nodes_out[nodes.index(edge["QerId"])] + 1
        else:
            nodes.append(edge["QerId"])
            nodes_in.append(0)
            nodes_out.append(1)

        if edge["AerId"] in nodes:
            nodes_in[nodes.index(edge["AerId"])] = nodes_in[nodes.index(edge["AerId"])] + 1
        else:
            nodes.append(edge["AerId"])
            nodes_in.append(1)
            nodes_out.append(0)


    in_weight = []
    out_weight = []
    combined = []
    weights = []

    for i in range(len(nodes)):
        tmp = str(nodes_in[i]) + " " + str(nodes_out[i])

        if tmp in combined:
            weights[combined.index(tmp)] = weights[combined.index(tmp)]+1
        else:
            combined.append(tmp)
            in_weight.append(nodes_in[i])
            out_weight.append(nodes_out[i])
            weights.append(1)

    for i in range(len(combined)):
        writer.writerow({"In-degree": in_weight[i], "Out-degree": out_weight[i], "Weight": weights[i]})
    csvfile.close()

def ReputationAndAnswerInterval():
    collection = cn_mdb.javascript.find();
    timeInterval = []
    reputation = []
    for question in collection:
        try:
            question['owner']['reputation']
            question['answers']
        except Exception:
            "Information Missed"
        else:
            if len(question['answers'])>0:
                last_time = 0
                answer_time=[]
                for each_answer in question['answers']:
                    if each_answer['is_accepted']==True:
                        interval = (each_answer['creation_date']-question['creation_date'])/(60*60)
                        timeInterval.append(interval)
                        reputation.append(question['owner']['reputation'])

    csvfile = open("reputation_answer_interval.csv", "w")
    filednames = ["Reputation", "AnswerInverval"]
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()

    for i in range(len(timeInterval)):
        writer.writerow({"Reputation": reputation[i], "AnswerInverval": timeInterval[i]})
    csvfile.close()


#answerGroup()
#exportAnswerGroup()
#exportEdgeInfo()
# exportNodeWeights()
# exportNodeWeightsSize()
ReputationAndAnswerInterval()

