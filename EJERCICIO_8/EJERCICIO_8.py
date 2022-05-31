"""Cantidad de números primos dentro del número N"""

x=int(input("Digite un número: "))
i = 1
c = 0

while i < x:
    if (i % 5) == 0:
        c = c + 1
    i = i + 1
print("Dentro del número", x, "hay", c, "números múltiplos de 5")