import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))


def rm(array):
    tmp = []
    stack = [array[0]]
    p, q = 0, 1
    while q <= len(array):
        if q == len(array):
            if q - p < m:
                tmp = tmp + stack
                break
            else:
                break
        if array[p] != array[q]:
            if q - p < m:
                tmp = tmp + stack
            stack = [array[q]]
            p = q
            q = p + 1
            continue
        else:
            stack.append(array[q])
            q += 1
    return tmp


while True:
    tmp = rm(arr)
    if tmp == arr or tmp == []:
        arr = tmp
        break
    arr = tmp

print(len(arr))
for i in arr:
    print(i)