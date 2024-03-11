import sys
input = lambda: sys.stdin.readline().rstrip()

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)
  
n = int(input())
if n == 0:
    print(0)
else:
    avg = my_round(n*0.15)
    opi = []
    for _ in range(n):
        opi.append(int(input()))

    if avg != 0:
        opi = sorted(opi)[avg:-avg]
        print(my_round(sum(opi)/len(opi)))
    else:
        print(my_round(sum(opi)/len(opi)))
