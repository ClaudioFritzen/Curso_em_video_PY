""" for c in range (1,4):
    n = int(input('Digite um numero: ' ))
    print(c)
print('FIM')

 """


""" c = 1

while c < 10:
    print(c)
    c = c +1
print(c) """

""" n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM') """

""" r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM') """

""" n = 1 
while n != 0:
    n = int(input('Digite um numero: '))
print()
 """

""" 
 quero saber quantos numeros eram pares e impares
"""

p = 0
i = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))

    if n !=0:

        if n % 2 == 0:
            p += 1
        else:
            i += 1

print(f' voce digitou {p} numeros pares e {i} numeros impares')
