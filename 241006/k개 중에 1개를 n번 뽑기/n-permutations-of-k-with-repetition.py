import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = [i for i in range(1, k+1)]

def permutation(n, new_arr):
    global arr

    if len(new_arr) == n:
        print(*new_arr)
        return
    for i in range(len(arr)):
        permutation(n, new_arr + [arr[i]])

permutation(n, [])