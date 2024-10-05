import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        answer = max(answer, sum(arr[i][j:j+3]) + sum(arr[i+1][j:j+3]) + sum(arr[i+2][j:j+3]))
print(answer)