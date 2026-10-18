#Импорт random
import time
import random
#Переменные для создания списков
a = []
b1 = []
b2 = []
#Переменные для сортироки
m = 0
t = 0
#Переменные для подсчёта количества сравнений
k1 = 0
k2 = 0
#Создание списка с случайными элементами
start = time.time()
for i in range(0,100000):
    a.append(random.randint(0,100000))
    b1 = a.copy()
#Сортировка алгоритмом пузырька
# end = time.time()
# t = end - start
# print(f"Создание : {t} сек.\n")


# start = time.time()
# for i in range(0,100000):
#     t=0
#     for j in range(len(a)-1):
#         if a[j]<a[j+1]: #Сравнение соседних элементов
#             s=a[j]
#             a[j]=a[j+1]
#             a[j+1]=s
#             t=1
#             k1+=1
#     if t == 0:
#             break
# end = time.time()
# t = end - start
# print(f"Пузырек : {t} сек.\n")
#Сортика алгортмом выбора
start = time.time()
for i in range(len(b1)-1):
    m = b1[0]
    for i in range(0, len(b1)): #Поиск наибольшего элемента
        if b1[i] > m:
            m = b1[i]     
    b1.remove(m) #Удаление из начального списка
    b2.append(m) #Добавить в отсортированный список
    k2+=1
end = time.time()
t = end - start
print(f"Выбором : {t} сек.\n")
#Вывод результатов
# print('\nОтсортированный список:\n')
# print(a)
# print('\nКоличество сравнений в сортировке пузырьком:',k1)
# print('Количество сравнений в сортировке выбором:',k2)
