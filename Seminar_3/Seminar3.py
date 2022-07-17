# Task 1: Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''
massive = [123, "ASD", 5, "fun", 0, "cold"]

def findNumberInMassive(userNumber):
        if userNumber in massive:
            print("This number is in the list ")
        else:
            print("This number is not in the list ")

userNum = int(input("insert a number: "))
findNumberInMassive(userNum)
'''
# Task 2: Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет

massive = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

def findNumberInMassive(userWords):
        if userWords in massive:
            print("This word is in the list ")
            index = massive.index(userWords)
            print(index)
        else:
            print("This word is not in the list ")

userWord = input("insert a number: ")
findNumberInMassive(userWord)