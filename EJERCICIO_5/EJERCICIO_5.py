"""Calcular la cantidad de veces que sale el número 3
al lanzar N veces un dado"""
import random
n = int(input("Digite cuántas veces lanzará el dado: "))
x = 0

while n > 0:
    y = random.randint(1,6)
    if y == 3:
        x = x + 1
    n = n - 1
print("Las veces que aparece el número 3 al lanzar el dado es: " + str(x))