import math
import random
from datetime import datetime

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print("Задача-1")
sourcelst = [2, -5, 8, 9, -25, 25, 4, 0]
print(sourcelst)
resultlst = []
for n in sourcelst:
    if n >= 0:
        chi = math.sqrt(n)
        if (chi-int(chi))==0:
            resultlst.append(int(chi))
print(resultlst)            
        


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("Задача-2")
print("{:%B %d, %Y}".format(datetime.now()))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print("Задача-3")
q = 0
maxq = 155
resultlst = []
while q < maxq:
    randintv = random.randint(-100,100)
    resultlst.append(randintv)
    q = q + 1
print(resultlst)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print("Задача-4")
lst = [1, 2, 4, 5, 6, 2, 5, 2]
#remove double
setV = set(lst)
print(setV)
startind = 0

# inialize of map
mapv = dict.fromkeys(setV)

print(mapv)
for f in lst:
    indin = lst.index(f,startind)
#   print(str(f) +":" + str(indin))
    startind = startind + 1
    if mapv[f] != None:
        mapv[f]= mapv[f] + 1
    else:
        mapv[f] = 1

reslist = []

for key,value in mapv.items():
    if value == 1:
        reslist.append(key)
    

print(reslist)




