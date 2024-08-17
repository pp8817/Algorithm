import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)


arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def sol(arr):  
    if len(arr) == 0:
        return
    
    tempL, tempR = [], []
    root = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > root:
            tempL = arr[1:i]
            tempR = arr[i:]
            break
    else:
        tempL = arr[1:]
    sol(tempL)
    sol(tempR)
    print(root)

sol(arr)