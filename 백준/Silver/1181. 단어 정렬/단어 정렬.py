n = int(input())
arr = []
ex = []
for _ in range(n):
    st = input()
    le = len(st)
    if st in ex:
        continue
    else:
        arr.append([le, st])
    ex.append(st)
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[1])