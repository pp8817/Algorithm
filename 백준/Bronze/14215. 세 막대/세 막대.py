li = list(map(int,input().split()))
li.sort()
v = sum(li[:2])
if max(li)<v:
    print(sum(li))
else:
    print(2*v-1)