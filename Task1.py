#Задача №1________________________________________________

def sum():
    N = input("Введите число: ")
    formula = f'{N} + {N+N} + {N+N+N}'
    print(f"{formula} = {eval(formula)}")

sum()
