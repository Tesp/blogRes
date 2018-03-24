import requests
import json
import time
import hashlib

# 获取毫秒数
t = time.time()

# print (t)                       #原始时间数据
# print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳
# nowTime = lambda:int(round(t * 1000))
# print (nowTime());              #毫秒级时间戳，基于lambda
#
# print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化


# 加密
kk=hashlib.md5(b'123').hexdigest()
print(kk)
# 开始倒计时
time.sleep(4)
