s = input()
li = list(-1 for _ in range(26))
n = 0
for i in s:
    if li[ord(i)-97] == -1:
        li[ord(i)-97] = n
        
    n+=1
print(" ".join(map(str, li)))

# S = input()

# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(x), end = ' ')
