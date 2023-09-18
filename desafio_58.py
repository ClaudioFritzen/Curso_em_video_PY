'''
melhore o jogo do desafio 28 onde o computador vai
pensar em um numero entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando 
no final quantos palpites foram necessario para vencer
'''
import random
inicio = 0
tentativas = 0
usuario = 1
lista = [1,2,3,4,5,6,8,9]

while usuario != 0:
    usuario = int(input('Digite um numero de 1 a 10: '))
    for na in lista.random():
        print(na)
print('Fim do programa!!')