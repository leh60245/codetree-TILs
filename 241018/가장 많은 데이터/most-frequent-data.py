n = int(input())
save_key = dict()
answer = []
for _ in range(n):
    color = input()
    if color in save_key:
        answer[save_key[color]] += 1
    else:
        save_key[color] = len(answer)
        answer.append(1)

print(max(answer))