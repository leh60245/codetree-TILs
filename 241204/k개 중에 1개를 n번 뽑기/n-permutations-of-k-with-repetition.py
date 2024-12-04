K, N = map(int, input().split())

def per(n, ans):
    if n == 0:
        print(*ans)
        return
    for i in range(1, K+1):
        per(n-1, ans + [i])

per(N, [])