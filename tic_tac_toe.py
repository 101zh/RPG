from collections import OrderedDict

leaders = dict()


def processData(data: dict):
    for x in data:
        print(x)
    p1name = data.get("player1name")
    p2name = data.get("player2name")
    score1 = data.get("score1")
    score2 = data.get("score2")

    if p1name in leaders.keys():
        leaders[p1name] = processScore(score1)+leaders.get(p1name)
    else:
        leaders[p1name] = processScore(score1)

    if p2name in leaders.keys():
        leaders[p2name] = processScore(score2)+leaders.get(p2name)
    else:
        leaders[p2name] = processScore(score2)
        
    return sortDict(leaders)

def processScore(score: str):
    if score == "win":
        return 1
    elif score =="lose":
        return -1
    else:
        return 0

def sortDict(dictionary:dict):
    list = []
    ordered_dict = OrderedDict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))
    for item in ordered_dict.items():
        dict1 = {item[0]:item[1]}
        list.append(dict1)
    return list