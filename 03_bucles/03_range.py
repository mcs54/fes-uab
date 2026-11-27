###
# EXERCICIS (range)
###

print('Exercici 1:') # Imprimir números de l'1 al 10
# Imprimeix els números de l'1 al 10 (inclosos) fent servir un bucle for i range().

for num in range(1, 11, 1):
    print(f'{num}')

print('Exercici 2:') # Imprimir números senars de l'1 al 20
# Imprimeix tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().

for num in range(1, 21, 1):
    if num % 2 != 0:
        print(f'{num}')

print('Exercici 3:') # Imprimir múltiples de 5
# Imprimeix els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().

for num in range(5, 51, 5):
    print(f'{num}')

print('Exercici 4:') # Imprimir números en ordre invers
# Imprimeix els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
for num in range(10, 0, -1):
    print(f'{num}')

print('Exercici 5:') # Suma de números en un rang
# Calcula la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
sum = 0
for num in range(1, 101, 1):
    sum += num
print(f'{sum}')

print('Exercici 6:') # Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().

num = int(input('Entra un numero: '))
for i in range(1, 11, 1):
    res = num * i
    print(f'{num} * {i} = {res}')
    res = 0
