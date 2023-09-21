li = []
le = 0
result = ""
for i in range(5):
    a = input()
    li.append(list(a))
    if len(a)>=le:
        le=len(a)
for j in range(le):
    for i in li:
        if len(i)-1>=j:
            result+= i[j]
print(result)