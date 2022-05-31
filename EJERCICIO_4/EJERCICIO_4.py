"""Determinar si un número es capicúa o no"""

n=int(input("Digite un número: "))
nc = n
x = 0
r = 0

while n > 0:
    r = n % 10
    x = x * 10 + r
    n = n // 10
    
if x == nc:
    print("El número es capicúa")
else:
    print("El número no es capicúa")

  