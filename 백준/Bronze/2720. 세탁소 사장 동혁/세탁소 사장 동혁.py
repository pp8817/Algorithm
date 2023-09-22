T = int(input())
li = [25,10,5,1]

for i in range(T):
    c = int(input())
    
    for j in li:
        a = c//j
        c = c % j;
        print(a, end=" ")