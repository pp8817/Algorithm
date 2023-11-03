def solution(n):
    
    h = len(n[0])
    n = "".join(n)

    row = set()
    col = set()
    
    r = 0
    c = 0
    for i in n:
        if i == "#":
            row.add(r)
            col.add(c)
        
        c+=1
        if c == h:
            c = 0
            r += 1

    return [min(row), min(col), max(row)+1, max(col)+1]