from itertools import combinations
from collections import defaultdict

def solution(infos, querys):
    
    answer = []
    info_dict = defaultdict(list)
    
    for info in infos:
        temp = info.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        
        for i in range(5):
            combi = list(combinations(conditions, i))
            
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()
    for query in querys:
        query = query.split(" ")
        query_score = int(query[-1])
        query_key = query[:-1]

        for _ in range(3):
            query_key.remove("and")

        while "-" in query_key:
            query_key.remove("-")
        query_key = ''.join(query_key)

        if query_key in info_dict:
            scoreList = info_dict[query_key]

            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= query_score:
                        right = mid
                    else:
                        left = mid+1
                answer.append(len(scoreList)-left)
        else:
            answer.append(0)

    return answer


p_info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
p_query =["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(p_info, p_query))