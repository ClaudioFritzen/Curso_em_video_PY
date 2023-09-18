'''
 Faça um programa que leia o sexo de uma pessoa. mas
 so aceite os valores 'M' ou 'F'. Caso estaja errado, 
 peça para digitar novamente até ter um valor correto.
'''


print('aceito apenas "M" ou "F"')
valor = str(input('Digite seu sexo ')).upper()
print(type(valor))

 

""" valor = 1
while valor != 0:
    if valor == 0:
        print('Fim do programa')
    
valor = int(input('Digite seu sexo: ')).upper()
print(valor) """