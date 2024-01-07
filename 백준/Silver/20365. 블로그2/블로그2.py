import sys
input = sys.stdin.readline

N = int(input())
s = input()

dic = {"R":0, "B":0}
dic[s[0]] += 1
for i in range(1, N):
    if s[i] != s[i-1]:
        dic[s[i]]+=1
result = min(dic['B'], dic['R'])+1
print(result)
    