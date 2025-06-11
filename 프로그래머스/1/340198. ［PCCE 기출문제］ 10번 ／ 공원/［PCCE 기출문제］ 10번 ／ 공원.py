def solution(mats, park):
    
    def access(mat, park, st_row, st_col):
        for r in range(st_row, st_row+mat):
            for c in range(st_col, st_col+mat):
                if r >= R or c >= C or park[r][c] != "-1":
                    return False
        return True
    
    R, C = len(park), len(park[0])
    mats.sort(reverse = True)
    
    for mat in mats:
        for r in range(R-mat+1):
            for c in range(C-mat+1):
                if access(mat, park, r, c):
                    return mat
                
    return -1