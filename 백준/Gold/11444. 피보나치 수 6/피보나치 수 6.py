import sys
input = sys.stdin.readline

MOD = 1000000007

def matrix_mult(a, b, mod=MOD):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod]
    ]

def matrix_power(mat, n, mod=MOD):
    if n == 1:
        return mat
    elif n % 2 == 0:
        half_mat = matrix_power(mat, n // 2, mod)
        return matrix_mult(half_mat, half_mat, mod)
    else:
        return matrix_mult(mat, matrix_power(mat, n - 1, mod), mod)

def fibonacci(n, mod=MOD):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        base_matrix = [[1, 1], [1, 0]]
        return matrix_power(base_matrix, n - 1, mod)[0][0]

N = int(input())
print(fibonacci(N) % MOD)
