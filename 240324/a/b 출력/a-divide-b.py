a, b = map(int, input().split())
answer = ""
some = a // b
answer = f"{some}."
a = a % b
cnt = 0
cnt_zero = 0
while True:
    if a == 0 or cnt > 19 :
        break
    if a // b == 0:
        a *= 10
        cnt_zero += 1
        continue
    answer += "0" * (cnt_zero-1)
    some = a // b
    answer += str(some)
    a = a % b
    cnt += 1 + (cnt_zero-1)
    cnt_zero = 0

last = len(answer.split('.')[-1])
if last < 20:
    answer += '0' * (20-last)
print(answer)