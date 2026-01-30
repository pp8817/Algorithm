import sys
input = lambda: sys.stdin.readline().rstrip()

def count_odd(n_str):
    cnt = 0
    for char in n_str:
        if int(char) % 2 != 0:
            cnt += 1
    return cnt

def solve(n_str, current_odds):
    global min_ans, max_ans

    current_odds += count_odd(n_str)

    if len(n_str) == 1:
        min_ans = min(min_ans, current_odds)
        max_ans = max(max_ans, current_odds)
        return 

    elif len(n_str) == 2:
        new_n = str(int(n_str[0]) + int(n_str[1]))
        solve(new_n, current_odds)
    
    else:
        n = len(n_str)
        for i in range(1, n-1):
            for j in range(i+1, n):
                part1 = n_str[:i]
                part2 = n_str[i:j]
                part3 = n_str[j:]

                new_n = str(int(part1) + int(part2) + int(part3))
                solve(new_n, current_odds)


N = input()
min_ans, max_ans= float('inf'), 0
solve(N, 0)
print(min_ans, max_ans)
