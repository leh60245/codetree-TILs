n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)
set2 = set(arr2)


for v2 in arr2:
    if v2 not in set1:
        print(0, end=' ')
    else:
        print(1, end=' ')