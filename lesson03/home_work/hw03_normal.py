# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachhi(startn, stopn):
   ret_list = [1,1]
   for n in range(2, stopn):
       ret_list.append(ret_list[n-1]+ret_list[n-2])
   print(ret_list[startn:stopn])
#   return ret_list{}
fibonachhi(3,11)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def find_max(lst):
    for n in range(0,len(lst)):
        for n in range(0,len(lst)):
            if n == 0:
                continue
            if lst[n] > lst[n-1]:
                felement = lst[n-1]
                lst[n-1] = lst[n]
                lst[n] = felement
    print(lst)

find_max([0,1,23,4,7])



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# example  filter
def custom_filter(lst,startval,sign,endval):
    retLst = []
    if sign == None:
        return "Error: sign not defined"

    def filterIn(val,startval,sign,endval):
        if startval != None and endval != None :
            if sign == "INB":
                return val >= startval and val <= endval
            elif sign == "IN":
                 return val > startval and val < endval
            elif sign == "OUT":
                 return val < startval or val > endval
            elif sign == "OUTB":
                 return val <= startval or val >= endval
            else:
                return False
        elif startval != None and endval == None :
             if sign == ">":
                 return val > startval
             elif sign == "<":
                 return val < startval
             elif sign == ">=":
                 return val >= startval
             elif sign == "<=":
                 return val <= startval
             elif sign == "==":
                 return val == startval
             else:
                return False
        elif endval != None and startval == None :
             if sign == ">":
                return val > endval
             elif sign == "<":
                 return val < endval
             elif sign == ">=":
                 return val >= endval
             elif sign == "<=":
                 return val <= endval
             elif sign == "==":
                 return val == endval
             else:
                return False
#   look at every element in the list
    for ele in lst :
        if filterIn(ele,startval,sign,endval):
            retLst.append(ele)
    return retLst;

#
res = custom_filter([-1,1,2,3,4,5,6,7,100],1,"OUT",55)
print(res)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
