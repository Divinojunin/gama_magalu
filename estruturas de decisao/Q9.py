#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("1º número: "))
n2 = int(input("2º número: "))
n3 = int(input("3º número: "))
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux
if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux
print(n1, n2, n3)