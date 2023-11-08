string = input()
answer = ''.join([string[i] for i in range(1, len(string), 2)])
print(answer[::-1])