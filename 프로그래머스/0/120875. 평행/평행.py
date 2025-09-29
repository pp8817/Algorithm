def is_parallel(p1, p2, p3, p4):
    dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
    dx2, dy2 = p4[0] - p3[0], p4[1] - p3[1]
    return dx1 * dy2 == dx2 * dy1  # 외적 == 0 → 평행

def solution(dots):
    return int(
        is_parallel(dots[0], dots[1], dots[2], dots[3]) or
        is_parallel(dots[0], dots[2], dots[1], dots[3]) or
        is_parallel(dots[0], dots[3], dots[1], dots[2])
    )