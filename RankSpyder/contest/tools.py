from .models import Contest, Rank, Submition
import pandas as pd

def saveSubmitions(contestid, data):
    Submition.objects.filter(localContestId=contestid).delete()
    for index, row in data.iterrows():
        Submition(
            localContestId=contestid,
            userId=row["username"],
            problemId = row["pid"],
            submitTime=row["time"],
            status=row["statue"]
        ).save()

def makeRankFromSubmitions(contestid, problems):
    Rank.objects.filter(localContestId=contestid).delete()
    submitions = Submition.objects.filter(localContestId=contestid)
    alldata = {}
    zeros = [0 for _ in range(problems)]
    for submition in submitions:
        problem = submition.problemId
        statue = submition.status
        username = submition.userId

        if username not in alldata.keys():
            alldata[username] = zeros.copy()

        if alldata[username][problem] <= 0:
            if statue == 1:
                alldata[username][problem] *= -20 * 60
                alldata[username][problem] += submition.submitTime
            elif statue == -1:
                alldata[username][problem] -= 1
    print(alldata)

    ls = []
    for uid, d in alldata.items():
        dic = {}
        dic["username"] = uid
        dic["ac"] = 0
        dic["time"] = 0
        dic["ac_detail"] = ''
        for t in d:
            if t > 0:
                dic["ac"] += 1
                dic["time"] += t
            dic["ac_detail"] += str(t) + ','
        dic["time"] //= 60
        dic["ac_detail"] = dic["ac_detail"][:-1]
        ls.append(dic)
    print(ls)
    
    df = pd.DataFrame(ls)
    df["time"] *= -1
    df.sort_values(by=["ac","time"], inplace=True, ascending=False)
    df["time"] *= -1
    df["rank"] = [i for i in range(1, df.shape[0]+1)]
    
    for index, row in df.iterrows():
        Rank(
        localContestId=contestid,
        userId=row["username"],
        ac = row["ac"],
        time=row["time"],
        rank=row["rank"],
        ac_detail=row["ac_detail"]
    ).save()
