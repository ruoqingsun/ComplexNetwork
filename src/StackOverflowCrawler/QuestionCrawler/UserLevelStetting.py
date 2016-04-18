from pymongo import MongoClient
import pprint

MONGODB_URI = 'mongodb://localhost:27017/cn'
client = MongoClient(MONGODB_URI)
cn_mdb = client['cn']

def userLevelsSetting():
    usersInfo = cn_mdb.usersInfo.find()

    for info in usersInfo:

        if info["reputation"] > 2000:
            cn_mdb.usersInfo.find_one_and_update(
                {"id": info["id"]},
                {"$set":{"category": "Expert", "level": 5}}
            )
        elif info["reputation"] > 1000:
            cn_mdb.usersInfo.find_one_and_update(
                {"id": info["id"]},
                {"$set": {"category": "Professional", "level": 4}}
            )
        elif info["reputation"] > 500:
            cn_mdb.usersInfo.find_one_and_update(
                {"id": info["id"]},
                {"$set": {"category": "User", "level": 3}}
            )
        elif info["reputation"] > 200:
            cn_mdb.usersInfo.find_one_and_update(
                {"id": info["id"]},
                {"$set": {"category": "Learner", "level": 2}}
            )
        elif info["reputation"] >= 1:
            cn_mdb.usersInfo.find_one_and_update(
                {"id": info["id"]},
                {"$set": {"category": "Newbie", "level": 1}}
            )

userLevelsSetting()
