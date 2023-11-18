m1, d1, m2, d2 = map(int, input().split())
input_weekend = input()
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
answer = 0

def add_seven_day(m1, d1, gap):
    new_m1 = m1 + 1 if (d1 + gap) // (days[m1] + 1) else m1
    new_d1 = (d1 + gap) % (days[m1] + 1) 
    if new_d1 < 7:
        new_d1 += 1
    m1 = new_m1
    d1 = new_d1
    return m1, d1

gap = weeks[input_weekend] - weeks["Mon"]
m1, d1 = add_seven_day(m1, d1, gap)
if (m1 < m2) or (m1 == m2 and d1 <= d2):
    answer += 1

gap = 7
while True :
    m1, d1 = add_seven_day(m1, d1, gap)
    if (m1 < m2) or (m1 == m2 and d1 <= d2):
        answer += 1
        continue
    break

print(answer)