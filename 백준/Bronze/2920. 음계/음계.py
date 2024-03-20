import sys
input = lambda: sys.stdin.readline().rstrip()


ascending = [1,2,3,4,5,6,7,8]
descending=[8,7,6,5,4,3,2,1]
li = list(map(int, input().split()))

if li == ascending:
    print("ascending")
elif li == descending:
    print ("descending")
else:
    print("mixed")
