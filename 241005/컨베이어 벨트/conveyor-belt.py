import sys
input = sys.stdin.readline
n, t = map(int, input().split())
arr = []
arr = arr + list(map(int, input().split()))
arr = arr + list(map(int, input().split()))
idx = t % (n * 2)

arr = arr[-idx:] + arr[:-idx]

print(*arr[:n])
print(*arr[n:])