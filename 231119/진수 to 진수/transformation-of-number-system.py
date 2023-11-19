a, b = map(int, input().split())
n = input()
m = len(n)


cnt = 0
for idx, i in enumerate(n):
    cnt += a ** (m-idx-1)


answer = ''
while True:
    answer = str(cnt % b) +answer
    cnt //= b
    if cnt > 0:
        continue
    break


print(answer)