n, s = map(int, input().split())
arr = list(map(int, input().split()))
couple_arr = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        couple_arr.append(arr[i] + arr[j])
couple_arr = sorted(couple_arr)

sum_arr = sum(arr)
answer = abs(s - sum_arr + couple_arr[0])
for i in couple_arr[1:]:
    k = abs(s - sum_arr + i)
    if answer >= k:
        answer = k
        continue
    break
print(answer)