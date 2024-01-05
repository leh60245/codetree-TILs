people1 = list(map(str, input().split()))
people2 = list(map(str, input().split()))
people3 = list(map(str, input().split()))
peoples = [people1, people2, people3]

def is_yes(people):
    answer = True if people[0] == "Y" and int(people[1]) >= 37 else False
    return answer

answer = "E" if sum([1 for people in peoples if is_yes(people)]) >= 2 else "N"
print(answer)