#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input("Qual turno que você estuda: M - matutino; V - vespertino ou N - noturno: "))

if turno == 'M' or turno == 'm':
    print('Bom dia!')
if turno == 'V' or turno == 'v':
    print('Boa tarde!')
if turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Valor inválido.\n Por favor tente novamente:[M, V, N]...')