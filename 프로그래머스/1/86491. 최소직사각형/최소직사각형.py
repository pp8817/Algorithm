def solution(sizes):
    w, h = 0, 0
    
    for size in sizes:
        if size[0] > size[1]:
            w = max(w, size[0])
            h = max(h, size[1])
        else:
            w = max(w, size[1])
            h = max(h, size[0])
    
    return w*h