# Task 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def countNumbersInNumber(userNumber):
    counts = 0
    while userNumber > 0:
        counts += userNumber % 10
        userNumber //= 10
    return counts

userNumb = int(input("Insert a number: "))
print(countNumbersInNumber(userNumb))


# Task 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
'''
def setOfProductsOfNumbers(userNumber):
   count = 1
   sum = 1
   while count <= userNumber:
    sum = count * sum
    print(sum, end = " ")
    count += 1

userNumb = int(input("Insert a number: "))
setOfProductsOfNumbers(userNumb)
'''