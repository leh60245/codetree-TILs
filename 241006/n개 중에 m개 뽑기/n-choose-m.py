import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = []


def con(cnt, idx):  # cnt: 위치
    if cnt == m:
        print(*answer)
        return
    for i in range(idx, len(arr)):
        answer.append(arr[i])
        con(cnt+1, i+1)
        answer.pop()

con(0, 0)