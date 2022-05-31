"""Cantidad de un número que contiene un rango"""

x=int(input("Ingrese el número inicial del rango: "))
y=int(input("Ingrese el número final del rango: "))
c = 0
i = x + 1

while i < y:
    c = c + 1
    i = i + 1

print("La cantidad de números dentro del rango indicado es", c)