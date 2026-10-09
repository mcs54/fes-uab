###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

print("Marti Carreras Serra\nPalamos")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a), type(b), type(c), type(d), type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

cadena = "1234"
print(f"Format int: {int(cadena)}\n")
print(f"Format float: {float(cadena)}\n")

num = 3.99
print(f"Format int: {int(num)}\n")

#Veiem com si fem un cast de int a un float em trunca el nombre per encomptes d'arrodonir-lo

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

nom = "Martí"
edat = 19
altura = 1.7

print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {altura} metres d'alçada")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

PI = 3.14159
resultat = int(round(PI) / 2)
print(f"El resultat és: {resultat}")


print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

temp_c = input("Entra una temperatura en graus Celsius: ")
temp_f = (int(temp_c) * 9/5) + 32

print(f"Temperatura en graus Celsius: {temp_c}\nTemperatura en graus Fahrenheit: {temp_f}\n")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

total_compte = input("Introdueix el total del compte del restaurant: ")
percentatge_propina = input("Quin percentatge de propina vols deixar? ")
propina = (int(percentatge_propina) / 100) * float(total_compte)
total_pagar = float(total_compte) + propina

print(f"La propina és de {propina:.2f}€, i el total a pagar és de {total_pagar:.2f}€")


print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contrasenya = input("Introdueix una contrasenya: ")
if len(contrasenya) != 8:
   print("Contrasenya no vàlida")
else: print("Contrasenya vàlida")
