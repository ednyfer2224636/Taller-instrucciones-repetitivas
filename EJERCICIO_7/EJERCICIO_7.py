"""Cantidad de números pares que contiene un rango"""

x=int(input("Ingrese el número inicial del rango: "))
y=int(input("Ingrese el número final del rango: "))

c = 0
i = x + 1

while i < y:
    print(str(i))
    if (i % 2) == 0:
        c = c + 1
    i = i + 1 

print("La cantidad de números pares dentro del rango indicado es", c)
