n, b = input().upper().split()
b = int(b)

li=[]

for i in n:
    a = ord(i)
    if 64<a<91:
        li.append(a-55)
    else:
        li.append(int(i))
result = 0
for i in range(len(li)):
    result += (b**i)*li[len(li)-i-1]
print(result)