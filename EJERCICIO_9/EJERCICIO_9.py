"""Determinar la cantidad de dígitos de un número"""

x=int(input("Digite un número: "))
c = 0

while x > 0:
    x = x // 10
    c = c + 1
print("El número tiene", c, "cifras")
