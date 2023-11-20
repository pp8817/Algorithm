def solution(s):
    ans = list(map(int, s.split()))
    return f"{min(ans)} {max(ans)}"