n = int(input())

answer = dict()
for _ in range(n):
    input_string = list(map(str, input().split()))
    if input_string[0] == 'add':
        answer[input_string[1]] = input_string[2]
    elif input_string[0] == 'remove':
        answer.pop(input_string[1])
    else:   # 'find'
        if input_string[1] in answer:
            print(answer[input_string[1]])
        else:
            print(None)