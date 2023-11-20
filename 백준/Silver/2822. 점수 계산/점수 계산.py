import sys
input = lambda: sys.stdin.readline().rstrip()
li = []
for i in range(1, 9):
    li.append([i, int(input())])
    
li.sort(key = lambda x :(x[1], x[0]))
s = 0
for i in range(1, 6):
    s += li[-i][1]
print(s)
answer = []
for i in range(3, 8):
    answer.append(li[i][0])
print(*(sorted(answer)))