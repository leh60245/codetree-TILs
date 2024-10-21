n, k = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0

count = dict()


for idx1 in range(len(arr)):
    for idx2 in range(idx1+1, len(arr)):
        third_num = k - (arr[idx1] + arr[idx2])
        if third_num in count:
            ans += count[third_num]


        if (arr[idx1] + arr[idx2]) not in count:
            count[(arr[idx1] + arr[idx2])] = 1
        else:
            count[(arr[idx1] + arr[idx2])] += 1

print(ans)