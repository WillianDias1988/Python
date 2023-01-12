"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


numero_digitado = input("Digite um numero inteiro: ")

while numero_digitado.isdigit():

    if numero_digitado.isdigit():
        if (int(numero_digitado) % 2 == 0):
            print("o numero é par")
        else:
            print("o numero é impar")
    else:
        print(f'{numero_digitado} precisa ser um numero inteiro!')

    numero_digitado = input("Digite um numero inteiro: ")
else:
    print(f'"{numero_digitado}" precisa ser um numero inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_digitada = input("Digite a hora para receber a saudação: ")

if hora_digitada.isdigit():

    hora_digitada = int(hora_digitada)

    if hora_digitada >= 18 and hora_digitada <= 23:
        print("Boa noite")
    elif hora_digitada >= 12 and hora_digitada <= 17:
        print("Boa tarde")
    elif hora_digitada >= 0 and hora_digitada <= 11:
        print("Bom dia")
else:
    print("Digite um horario valido para receber a saudação!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_digitado = input("Digite seu primeiro nome: ")

if not nome_digitado.isdigit():
    if len(nome_digitado) <= 4:
        print("Seu nome é curto")
    elif len(nome_digitado) > 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("você precisa digitar um nome valido!")
