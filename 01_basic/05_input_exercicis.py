###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

tecnic, xarxa = input("Quin tècnic hi ha al càrreg i quina xarxa s'està instalant? (Utilitza la coma com a separador) ").split(",")
print(f"Tècnic: {tecnic}\nXarxa: {xarxa}\n")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_cable = input("Entra la longitud del camble en Km: ")
v_transm = input("Entra la velocitat de transmissió en Gbps: ")
v_normalitzada = int(v_transm) / 8 #ja que considero que 1 GB = 8 Gb

t_transm = 1 / v_normalitzada

print(f"Calen {t_transm} segons\n")

#no s'utlitza la longitud_cable en aquest problema

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

nombre_hores = input("Entra el nombre d'hores de feina: ")
preu_hores = input("Entra el preu de les hores de feina: ")
preu_instal = input("Entra el preu d'instal·lació: ")
preu_material = input("Entra el preu del material: ")

cost = (int(nombre_hores) * int(preu_hores)) + int(preu_instal) + int(preu_material)
print(f"El cost de l'instal·lació total és: {cost}€")
