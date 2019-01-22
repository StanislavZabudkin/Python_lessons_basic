# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
   numberfloat = float(number)
   numr = int(ndigits)
   number1 = int(numberfloat*10**(ndigits+1))
   print(" input plural to 10 and to numr+1",str(number1))
   # delete
   number3 = int(number1/10)*10
   difn = number1-number3
   print(str(difn))
   # find difference
   if (difn > 4):
      number3 = (number3/10+1)/10**(ndigits)
   number3 = (number3/10)/10**(ndigits)
   print(" result ", str(number3))

my_round(1234577.7,3)



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
   if len(str(ticket_number)) < 6:
      return "Error ticket number < 6"
   num1 = int(ticket_number/10**3)
   num2 = ticket_number - num1*10**3
   print(" num 1", num1, " num2 ", num2 )

  # print()

   def calc_sum(num1):
      s1 = 0
      i = 0
      while True :
         i=i+1
         res1 = int(num1/10**i)*10**i
         dif = num1-res1
         if i > 1:
            dif = int(dif /10**(i-1))
         if dif == num1:
            s1 = s1 +dif;
            break;
         s1 = s1 +dif;
         if res1 == 0:
            break
      return s1

   s1 = calc_sum(num1)
   s2 = calc_sum(num1)
   print( " s1 ",s1, " s2 ", s2)



print(lucky_ticket(123006))
