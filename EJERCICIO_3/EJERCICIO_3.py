"""Determinar si un número es primo o no"""

x=int(input("Digite un número: "))
d = 2
n = 2

while n < x:
      if (x % n ) == 0:
            d = d + 1
      
      n = n + 1

if d == 2:
      print("El número es primo")
else: 
      print("El número no es primo" )