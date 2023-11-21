import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())

cho = 1
while K>cho:
    cho *= 2

print(cho, end =' ')

count = 0
while True:
    if K % cho == 0:
        print(count)
        break
    cho = cho//2
    count+=1
    