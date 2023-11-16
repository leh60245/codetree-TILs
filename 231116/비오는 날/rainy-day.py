n = int(input())

rain = []
original = []
for _ in range(n):
    ori = input()
    string = ori.split(" ")
    string[0] = list(map(int, string[0].split("-")))
    if string[-1] == "Rain":
        rain.append(string)
        original.append(ori)

y = 10000
m = 13
d = 32
answer = 0
for idx, i in enumerate(rain):
    if y > i[0][0]:
        y = i[0][0]
        m = i[0][1]
        d = i[0][2]
        answer = idx
        continue
    if y == i[0][0] and m > i[0][1]:
        y = i[0][0]
        m = i[0][1]
        d = i[0][2]
        answer = idx

        continue
    if y == i[0][0] and m == i[0][1] and d > i[0][2]:
        y = i[0][0]
        m = i[0][1]
        d = i[0][2]
        answer = idx

        continue
print(original[answer])