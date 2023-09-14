S = list(map(int, input().split()))
result=[1,1,2,2,2,8]
for i in range(6):
  result[i] -= S[i]
print(' '.join(map(str, result)))