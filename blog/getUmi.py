import requests
import json
import time
import hashlib


def mainMethond() :

    #1， 获取当前时间
    timeNow = time.time()
    timemillen = int(round(timeNow * 1000))  # 毫秒级时间戳
    timeStr = "%s" % timemillen
    print(timeStr)
    # 2，获得时间签名
    # hashlib.md5(b'123').hexdigest()
    timeSign = hashlib.md5(timeStr.encode(encoding='UTF-8')).hexdigest()
    # 3，当前用户userid
    userIdStr="1601620170212333289"
    resStr=getRewardInfo(userIdStr,timemillen,timeSign)

    # jsonStr = json.dumps(r.text)
    # 4,解析抽奖信息为json
    jsonData = json.loads(resStr)
    print(jsonData["errMsg"])
    print(jsonData["nextActivityTime"])
    sleepTime=0;
    try:
        sleepTime = (int(jsonData["nextActivityTime"])) // 1000 + 10
    except TypeError:
        print("type error  nextactivitytime is null")

    print(sleepTime)
    if jsonData["bizSucc"]:
         print("hahh")
    else:
         print("hehhe")


def getRewardInfo(userid,timemillen,timeSign) :
    kv = {"userId": userid, "stime": timemillen, "sign": timeSign, "version": "1.3.7", "token": "1.3.7",
          "appType": "864318035322131", "platformCode": "YOUMI", "activityName": "LONG_ACTIVITY"}

    r = requests.request("POST", "https://api.yomijinrong.com/front/getReceiveRedEnvelopeTime.do", data=kv)
    print(kv)
    print(r.text)
    return r.text


def getReward(userid,moneyStr,timemillen,timeSign) :
    kv = {"userId": userid, "stime": timemillen, "sign": timeSign, "version": "1.3.7", "token": "1.3.7",
          "appType": "864318035322131", "platformCode": "YOUMI", "activityName": "LONG_ACTIVITY", "deducts":  "[]", "money": "10.92"}

    r = requests.request("POST", "https://api.yomijinrong.com/front/grantReward.do", data=kv)
    print(kv)
    print(r.text)
    return r.text;

def getShareReward(userid,timemillen,timeSign) :
    kv = {"userId": userid, "stime": timemillen, "sign": timeSign, "version": "1.3.7", "token": "1.3.7",
          "appType": "864318035322131", "platformCode": "YOUMI", "activityName": "SHARING_REWARDS"}

    r = requests.request("POST", "https://api.yomijinrong.com/front/returnRewards.do", data=kv)
    print(kv)
    print(r.text)
    return r.text;

def doShareingReward(userid,reWardIndex,timemillen,timeSign) :
    kv = {"userId": userid, "stime": timemillen, "sign": timeSign, "version": "1.3.7", "token": "1.3.7",
          "appType": "864318035322131", "platformCode": "YOUMI", "activityName": "SHARING_REWARDS","index": reWardIndex}

    r = requests.request("POST", "https://api.yomijinrong.com/front/sharingRewards.do", data=kv)
    print(kv)
    print(r.text)
    return r.text;


mainMethond()
