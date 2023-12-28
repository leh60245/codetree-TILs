arr = {1:"John", 2:"Tom", 3:"Paul"}
number = int(input())
try:
    answer = arr[number]
    print(answer)
except:
    print("Vacancy")