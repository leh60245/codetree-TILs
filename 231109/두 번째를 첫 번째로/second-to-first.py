string = input()
target = string[1]
what = string[0]
answer = ''
for i in string:
    if i == target:
        answer += what
    else:
        answer += i
print(answer)