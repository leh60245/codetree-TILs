string = input()
for idx, char in enumerate(string):
    if char == 'e':
        string = string[:idx] + string[idx+1:]
        break
print(string)