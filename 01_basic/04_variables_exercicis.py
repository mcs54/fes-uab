###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_identificador = "Router_1"
on_off = "ON"
ubi = "Cerdanyola"

print(f"Dades de l'encaminador:\nNom: {nom_identificador}\nEstat: {on_off}\nUbicació: {ubi}\n")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos = 15
gb_consumits = 8
gb_restants = gb_inclosos - gb_consumits

print(f"Queden {gb_restants} GB\n")

gb_consumits = 12
gb_restants = gb_inclosos - gb_consumits
print(f"Queden {gb_restants} GB\n")
