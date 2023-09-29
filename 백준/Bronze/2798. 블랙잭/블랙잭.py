n, m=map(int, input().split())
#n: 카드의 개수, M: 카드의 합
li=list(map(int, input().split()))
#li: 카드에 적힌 수
arr=0
#3중 반복문을 통해서 모든 경우의 수 탐색
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if li[i]+li[j]+li[k]>m:
                continue
            else:
                arr=max(arr, li[i]+li[j]+li[k])
print(arr)