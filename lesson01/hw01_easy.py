
__author__ = 'Забудкин С.А.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

print("Please input number: ")
numStr = input("... ")
i = 0
while i < len(numStr):
    print(numStr[i]);
    i += 1

for i in numStr:
    print(i)






# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print("Please input number 1: ")
num1 = input("... ")

print("Please input number 2: ")
num2 = input("... ")

print(" num 1 : " + num1 + " num 2 : " + num2 )
num3 = num1
num1 = num2
num2 = num3
print(" num 1 : " + num1 + " num 2 : " + num2 )

(num1,num2) = (num2, num1)
print(" num 1 : " + num1 + " num 2 : " + num2 )

num1 = int(num2) - int(num1)
num2 = int(num2) - int(num1)
num1 = num2 + num1

print(" num 1 : " + str(num1) + " num 2 : " + str(num2) )


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print(" Please enter your age: ")
inputAge = input(... )
if int(inputAge) >= 18:
    print(" Access is allowed " )
else:
    print(" Access is not allowed ")
