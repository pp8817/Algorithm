import sys
input = lambda: sys.stdin.readline()

def backtranking(ans):
    if len(ans) == L:
        if check(ans):
            print("".join(ans))
            return
    
    for i in range(len(ans), C):
        if ans[-1] < arr[i]:
            ans.append(arr[i])
            backtranking(ans)
            ans.pop()

def check(ans):
    v_count, c_count = 0, 0
    
    for i in ans:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1
    
    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

vowel = ["a","e","i","o","u"] # 모음 리스트

# 모음 최소 1개, 자음 최소 2개
L,C = map(int, input().split())
arr = input().split()
arr.sort()

for i in range(C-L+1):
    a = [arr[i]]
    backtranking(a)