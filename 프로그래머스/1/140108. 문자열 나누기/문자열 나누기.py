
def solution(s):
    dic={}
    t = s[0]
    answer = 0
    dic["ex"]=0
    for i in range(len(s)):
        st = s[i]
        if st == t:
            if st not in dic:
                dic[st] = 1
            else:
                dic[st] += 1
        else:
            dic["ex"] += 1
        if dic[t] == dic["ex"]:
            answer+=1
            dic={"ex":0}
            if len(s)>=i+2:
                t = s[i+1]
    if len(dic)>=2:
        answer+=1
    return answer