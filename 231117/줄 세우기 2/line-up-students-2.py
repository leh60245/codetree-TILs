n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())) + [i+1])

arr = sorted(arr, key = lambda x : (x[0], -x[1]))
for i in range(n):
    print(*arr[i])