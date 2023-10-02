t=[]
for _ in range(5):
    t.append(int(input()))
print(int(sum(t)/len(t)))
t.sort()
print(t[2])