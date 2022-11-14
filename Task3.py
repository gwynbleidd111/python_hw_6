#Задача №3________________________________________________

import math

def simple_irreducible_fractions():
    N = int(input("Введите максимальный знаменатель: "))
    list = []
    for i in range(2,N+1):
        for j in range(1,i):
            if math.gcd(i,j) ==1:
                list.append(f"{j}/{i}")
    return list

print(simple_irreducible_fractions())
