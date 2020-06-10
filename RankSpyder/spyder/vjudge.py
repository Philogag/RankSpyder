

import pandas as pd
import numpy as np
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
header = {
'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
"referer": "https://vjudge.net/contest/365427"
}

loginid = {
    "username": "Philogag",
    "password": "okmjuhbgt00--"
}

def download_submitions(id: int, passwd: str, newLength=-1):
    rankurl = "http://vjudge.net/contest/rank/single/" + str(id)

    # 登录
    session = requests.Session()
    response = session.post("https://vjudge.net/user/login", loginid, headers=header)

    if response.status_code == 200:
        print("成功登录")
    else:
        print(response.status_code)
        print(response.text)

    # 读取数据
    response = session.get(rankurl)
    if response.status_code == 200:
        print("成功获取比赛数据")
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as e:
        print("Json Error:", response.text)
        raise e
    ret = {}

    submitions = np.array(data["submissions"])
    users = data["participants"]
    
    ret["contestId"] = data["id"]
    ret["contestName"] = data["title"]
    ret["problemNum"] = np.max(submitions[:, 1]) + 1
    ret["startTime"] = data["begin"] // 1000

    lasttime = data["length"] // 1000
    if newLength != -1:
        lasttime = newLength
    print(lasttime)
    
    ret["endTime"] = ret["startTime"] + lasttime

    pdd = pd.DataFrame(submitions, columns=["id", "pid", "statue", "time"])
    pdd = pdd.loc[pdd["time"] <= lasttime]
    pdd["statue"] = pdd["statue"].map({0: -1, 1: 1})
    
    users = [(_id, d[0]) for _id,d in users.items()]
    users = pd.DataFrame(users, columns=["id","username"])
    users["id"] = users["id"].astype(np.int32)

    ret["submitions"] = pd.merge(pdd, users, on='id', how='left')[["username", "pid", "statue", "time"]]

    print(ret)
    return ret

    
