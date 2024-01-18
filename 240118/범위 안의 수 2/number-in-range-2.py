answer = [0,0]
for _ in range(10):
    i = int(input())
    if 0 <= i and i <= 200 :
        answer[0] += i
        answer[1] += 1
answer[1] = answer[0]/answer[1]
print(f"{answer[0]} {answer[1]:.1f}")