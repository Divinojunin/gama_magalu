#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = int(input("Qual o preço do 1º produto: "))
produto2 = int(input("Qual o preço do 2º produto: "))
produto3 = int(input("Qual o preço do 3º produto: "))
if produto1 < produto2 and produto1 < produto3:
    print('1º produto é mais barato!')
elif produto2 < produto1 and produto2 < produto3:
    print('2º produto é mais barato!')
else:
    print('3º produto é mais barato!')