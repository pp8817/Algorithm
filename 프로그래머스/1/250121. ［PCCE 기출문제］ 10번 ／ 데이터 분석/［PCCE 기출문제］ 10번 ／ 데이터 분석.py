import sys
input = lambda: sys.stdin().readline().rtrip()

def solution(data, ext, val_ext, sort_by): 
    answer = []
    
    data_type={
        "code":0,
        "date":1,
        "maximum":2,
        "remain":3
    }
    filter_type = data_type[ext]
    for d in data:
        if d[filter_type]<val_ext:
            answer.append(d)
            
    sort_answer = sorted(answer, key=lambda x: x[data_type[sort_by]])
    
    return sort_answer