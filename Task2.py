#Задача №2________________________________________________

import random

def RandomList():
    SIZE = 15
    list = [random.randint(1,9) for i in range(SIZE)]
    print(list)
    return list

def Str_list(list):
    list = ''.join([str(x) for x in list])
    return list

def NumberSearch(list):
    number = input("Введите число: ")
    for i in list.split():
        if number in i:
            print("Да")
        else:
            print("Нет")

NumberSearch(Str_list(RandomList()))
