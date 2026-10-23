###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

num_1 = int(input("Entra el primer nombre: "))
num_2 = int(input("Entra el segon nombre: "))

if num_1 > num_2:
    print(f"{num_1} és més gran que {num_2}.")
else:
    print(f"{num_2} és més gran que {num_1}.")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num_1 = int(input("Entra el primer nombre: "))
num_2 = int(input("Entra el segon nombre: "))
op = input("Entra la operació que vols fer (+, -, *, /): ")

if op == "+":
    num_res = num_1 + num_2
    print(f"El resultat és: {num_res}")
elif op == "-":
    num_res = num_1 - num_2
    print(f"El resultat és: {num_res}")
elif op == "*":
   num_res = num_1 * num_2
   print(f"El resultat és: {num_res}")
elif op == "/":
    if num_2 == 0:
        print ("No pots dividir per 0")
        num_res = "ERROR"
        print(f"El resultat és: {num_res}")
    else: num_res = num_1 / num_2
else:
    print("Operació incorrecte")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Entra un any: "))
if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:
    print(f"{any} és un any de traspàs.")
else:
    print(f"{any} no és un any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Entra una edat: "))

if 0 <= edat <= 2:
    print("Nadó")
elif 3 <= edat <= 12:
    print("Infant")
elif 13 <= edat <= 17:
    print("Adolescent")
elif 18 <= edat <= 64:
    print("Adult")
elif 65 <= edat:
    print("Persona gran")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

nivell = int(input("Entra el nivell de la senyal (RSSI) en dBm: "))
if nivell >= -50:
    print("Cobertura excel·lent")
elif -67 <= nivell <= -50:
    print("Cobertura bona")
elif -75 <= nivell <= -67:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = int(input("Entra la potència òptica en dBm: "))

if -27 <= potencia <= -8:
    print("Nivell acceptable")
elif -8 < potencia:
    print("Nivell massa alt")
else:
    print("Nivell massa baix")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

gb_inclos = 20
consum = int(input("Entra el consum de dades en GB de la teva línia mòbil: "))

if 0 <= consum <= 20:
    print("El consum és dins del límit")
elif consum > 20:
    exces = consum - gb_inclos
    print(f"Has excedit {exces}GB de la teva tarifa")
else:
    print("Wow! GB negatius, ets un crack tio!")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

ind_LOS = int(input("Entra l'estat de l'indicador LOS (1: encès, 0: apagat): "))
ind_Internet = int(input("Entra l'estat de l'indicador d'internet (1: encès, 0: apagat):"))

if ind_LOS == 0 and ind_Internet == 1:
    print("Cal revisar el cable de fibra")

if ind_Internet == 0:
    print("Cal comprovar el servei del proveïdor")

if ind_LOS and ind_Internet == 1:
    print("La connexió sembla funcionar correctament")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bat = int(input("Entra el percentatge de bateria disponible del SAI: "))

if bat < 20:
    niv = "crític"
    print(f"El nivell és {niv}")
elif 20 <= bat <= 49:
    niv = "baix"
    print(f"El nivell és {niv}")
elif bat >= 50:
    niv = "suficient"
    print(f"El nivell és {niv}")
else:
    print("Valor fora de rang")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

lat = float(input("Entra la latència en [ms]: "))
perd = float(input("Entra el percentatge de paquets perduts: "))

if 0 < lat <= 30 and perd <= 1:
   print("Latència excel·lent")
elif 30 < lat <= 80 and perd <= 3:
   print("Latència bona")
elif 80 < lat <= 150 and perd <= 5:
    print("Latència acceptable")
elif lat < 0 or not(0 <= perd <= 100):
    print("Valor fora de rang")
else:
    print("Latència deficient")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input("Selecciona el tipus de plà (bàsic / plus): ")
gb_consum = float(input("Entra el consum mensual en GB: "))

if pla != "bàsic" or pla != "plus":
    print("No existeix aquest pla")
elif consum < 0:
    print("No hi ha consum negatiu")
elif pla == "bàsic":
    cost_tarifa = 10
    cost_gb_adicional = 1.5
    gb_inclos = 10

    if gb_consum > gb_inclos:
        gb_excedit = gb_consum - gb_inclos
        cost_exces = gb_excedit * cost_gb_adicional
    else:
        cost_exces = 0

    cost_total = cost_tarifa + cost_exces

    print(f"El cost total és: {cost_total}")
else:
    cost_tarifa = 20
    cost_gb_adicional = 0.75
    gb_inclos = 30

    if gb_consum > gb_inclos:
        gb_excedit = gb_consum - gb_inclos
        cost_exces = gb_excedit * cost_gb_adicional
    else:
        cost_exces = 0

    cost_total = cost_tarifa + cost_exces

    print(f"El cost total és: {cost_total}")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte_actiu = input("El compte està actiu? (y/n): ")
contrasenya_ok = input("La contrasenya és correcta? (y/n): ")

if compte_actiu == "y" and contrasenya_ok == "y":
    codi_doble_verif = input("El codi de doble verificació és correcte? (y/n): ")
    if codi_doble_verif == "n":
        acces = "denegat perque falla el codi"

if compte_actiu == "n":
    acces = "denegat per inactivitat"
elif contrasenya_ok == "n":
    acces = "denegat per contrasenya incorrecta"
else:
    acces = "permès"

print(f"L'accès queda {acces}")


# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router_on = input("El router està encès? (y/n): ")
los_on = input("L'indicador LOS del terminal òptic està encès? (y/n): ")
ind_router_on = input("L'indicador d'internet del router està encès? (y/n): ")

if (router_on != "y" or router_on != "n") or (los_on != "y" or los_on !=  "n") or (ind_router_on != "y" or ind_router_on !=  "n"):
    print("Entra un estat vàlid")
elif router_on == "n":
    print("Cal encendre el router")
elif los_on == "n":
    print("Cal revisar el cable de fibra")
elif ind_router_on == "n":
    print("Cal contactar amb el proveïdor")
else:
    print("La conexió funciona correctament")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

critic = input("La incidència afecta a un servei crític? (y/n): ")
usuaris = int(input("Quin és el nombre d'usuaris afectats?: "))
alternativa = input("Hi ha alguna alternativa? (y/n): ")

if (critic == "y" and alternativa == "n") or (usuaris >= 50 and alternativa == "n"):
    prioritat = "crítica"
elif usuaris >= 10 or critic == "y":
    prioritat = "alta"
else:
    prioritat = "baixa"
