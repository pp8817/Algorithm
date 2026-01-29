import sys
input = sys.stdin.readline

NONE, TOGGLE, SET0, SET1 = 0, 1, 2, 3

N, M = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (4 * N)
lazy = [NONE] * (4 * N)

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    build(node*2, start, mid)
    build(node*2+1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]

def apply(node, start, end, op):
    if op == SET0:
        tree[node] = 0
        lazy[node] = SET0
    elif op == SET1:
        tree[node] = end - start + 1
        lazy[node] = SET1
    elif op == TOGGLE:
        tree[node] = (end - start + 1) - tree[node]
        if lazy[node] == NONE:
            lazy[node] = TOGGLE
        elif lazy[node] == TOGGLE:
            lazy[node] = NONE
        elif lazy[node] == SET0:
            lazy[node] = SET1
        elif lazy[node] == SET1:
            lazy[node] = SET0

def push(node, start, end):
    if lazy[node] == NONE or start == end:
        return
    mid = (start + end) // 2
    apply(node*2, start, mid, lazy[node])
    apply(node*2+1, mid+1, end, lazy[node])
    lazy[node] = NONE

def update(node, start, end, l, r, op):
    if r < start or end < l:
        return
    if l <= start and end <= r:
        apply(node, start, end, op)
        return
    push(node, start, end)
    mid = (start + end) // 2
    update(node*2, start, mid, l, r, op)
    update(node*2+1, mid+1, end, l, r, op)
    tree[node] = tree[node*2] + tree[node*2+1]

def collect(node, start, end):
    if start == end:
        return [tree[node]]
    push(node, start, end)
    mid = (start + end) // 2
    return collect(node*2, start, mid) + collect(node*2+1, mid+1, end)

build(1, 0, N-1)

for _ in range(M):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        update(1, 0, N-1, b, b, SET1 if c == 1 else SET0)
    elif a == 2:
        update(1, 0, N-1, b, c-1, TOGGLE)
    elif a == 3:
        update(1, 0, N-1, b, c-1, SET0)
    else:
        update(1, 0, N-1, b, c-1, SET1)

print(*collect(1, 0, N-1))