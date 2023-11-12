import sys
input = lambda: sys.stdin.readline().rstrip()

# N = int(input())
# N_num = set(map(int, input().split()))

# M = int(input())
# M_num = map(int, input().split())

# for m in M_num:
#     if m in N_num:
#         print(1)
#     else:
#         print(0)

# set을 활용해서 풀었으나 문제 의도에 따라서 binary search를 활용하여 다시 풀이
def Binary_Search(left, right, m):
    
    while left<=right:
        mid = (left + right)//2
        if m == A[mid]:
            return 1
        elif m > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

N = int(input())
A = sorted(map(int, input().split()))

M = int(input())
M_num = map(int, input().split())

for m in M_num:
    print(Binary_Search(0, N-1, m))
