import random

s = int(input())
a = []
d = 2
m = 0

a = random.sample(range(10),10)
print(a)
l = len(a)
for i in range(l):
    if a[i] == s:
        print(i+1)
        break
if  i+1 == l:
    if a[i] != s:
        print('Элемент не найден')

while True:
    m = l//2+d
    if a[m] == s:
        print(m+1)
        break
    if a[m] > s:
        d = l//4
    if a[m] < s:
        print(m+1)
        d = -1//4
    print(m)

"""""
for m in range(l):
    if a[m] == s:
        print(m+1)
        break
if  m+1 == l:
    if a[m] != s:
        print('Элемент не найден')
"""""
