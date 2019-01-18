# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["apple","banan","kiwi","watermelon","pear"]
for i in fruits:
    print("{:>15}".format(i))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
fruits1 = ["apple","banan","kiwi","watermelon","pear"]
delfruits = ["apple","banan","kiwi"]
print(" ***** delete in one from another ***** ")
print(" from " )
print(fruits1)
print(" delete " )
print(delfruits)

j = 0
for j in delfruits:
    while True :
        if j in fruits1:
            fruits1.remove(j)
        else:
            break;
print(" result " )       
print(fruits1)
    



#print(newfruits)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst = [0,1,2,3,4,5,6,7,8,9]
#nwlst = lst.copy()
nwlst = [None] * len(lst)
i = 0
for p in lst:
    print(str(p) + " - " + str(p%2))
    if (p%2) == 0:
        nwlst[i] = p/4
    else:
        nwlst[i] = p*2
    i=i+1
print(" result " ) 
print(lst)        
print(nwlst)


