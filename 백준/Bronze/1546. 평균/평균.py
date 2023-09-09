n = int(input())
li = list(map(int, input().split()))
a = max(li)

for i in range(n):
    li[i] = li[i]/a*100
print(sum(li)/n)