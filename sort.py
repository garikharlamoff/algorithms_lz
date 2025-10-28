import random
a = []
b = []
k = 0
for i in range(0,10):
    a.append(random.randint(1,1_000))
b = a
for i in range(100):
    k=0
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            s=a[j]
            a[j]=a[j+1]
            a[j+1]=s
            k=1
    if k == 0:
            break
    print(a)     
print(i)  