import re

a = input()
b = input()
a = re.sub('[^0-9]','',a)
b = re.sub('[^0-9]','',b)
print(int(a)+int(b))