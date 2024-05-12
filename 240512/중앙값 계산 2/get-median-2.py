n = int(input())
arr = list(map(int, input().split()))
save = []
answer = []
for i in range(n):
    save.append(arr[i])
    if i % 2 == 0:
        save = sorted(save)
        answer.append(save[i//2])
print(*answer)