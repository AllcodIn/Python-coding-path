print("""\n 1.Créer une variable age de type int et affecte-lui un âge de ton choix 
Ensuite, affiche un message avec ton âge, par exemple : 'J\'ai 25 ans' """)

age = 19
print(f"J'ai {age} ans")

print("""2.Créer une variable prix de type float et affecte-lui un prix (par exemple, 15.99).
Ensuite, crée une variable quantite de type int pour représenter le nombre d'articles.
Calcule le coût total des articles (prix * quantité) et affiche le résultat.""")

prix = 15.99
quantite = 5
print(prix * quantite)

print("""3.Créer une liste fruits contenant 5 types de fruits de ton choix.
Puis :
Affiche le troisième fruit de la liste.
Ajoute un fruit supplémentaire à la fin de la liste.
Affiche la longueur de la liste.""")

fruits = ["Mangue", "Pomme", "Orange", "Bannane", "fraise"]
print(fruits[3])
fruits.append("pasteque")
print(len(fruits))

print("""4.Créer un dictionnaire personne avec les informations suivantes :
"nom" (clé) : ton prénom
"age" (clé) : ton âge
"ville" (clé) : ta ville Affiche une phrase qui combine ces informations (ex. : "Je m'appelle [nom], j'ai [age] ans et j'habite à [ville].")""")

personne = {
    "nom" : "TRAORE",
    "age" : 19,
}
personne["ville"] = print(f"Je m'appelle {personne["nom"]}, j'ai {personne["age"]} ans et j'habite à OUAGADOUGOU")

print("""5.Créer un tuple coordonnees avec deux éléments représentant ta position géographique (latitude, longitude).
Ensuite, affiche ces coordonnées sous la forme 'Latitude : [latitude], Longitude : [longitude]'.""")

coordonnees = (2500, 1000)

print(f"latitude: {coordonnees[0]}", end="")
print(f"logitude: {coordonnees[1]}", end="")

print("""6.Créer un ensemble nombres contenant quelques nombres aléatoires (par exemple, 1, 3, 5, 7, 9).
Ajoute un nombre à l'ensemble.
Affiche l'ensemble pour voir le résultat.
Essaie d'ajouter un nombre déjà présent et affiche à nouveau l'ensemble (tu devrais voir qu'il ne contient pas de doublons).""")

nombres = {1,3,5,7,9}

nombres.add(10)
print(nombres)
nombres.add(7)
print(nombres)
# NB: Un set ne garde qu’une seule occurrence de chaque élément, même si on essaie d’en ajouter plusieurs fois.