"""Factorial de un número entero"""

n= int(input("Digíte un número: "))
x = n
fac = 1

while n > 0:
    fac = fac * n
    n = n - 1

print("El factorial de", str(x), "es ", str(fac))