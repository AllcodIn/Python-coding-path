print("""Exercice 1 - Assignation simple : Crée une variable mon_nom et assigne-lui ton prénom. Affiche-le ensuite à l'écran.""")

mon_nom = "Ibrahim Khalil"
print(f"\n{mon_nom}")

print("""\n Exercice 2 - Réassignation de variables : Crée une variable age et assigne-lui un âge. Puis réassigne cette variable à un nouvel âge et affiche-le.""")
age = 19
print(f"\n{age}")

age = age + 1
print(f"\n{age}")

print("""Exercice 3 - Variables dans une fonction : Crée une fonction afficher_nom qui prend un prénom en argument et l'affiche à l'écran.""")

def afficher_nom(nom):
    print(f"\nJe suis {nom}")

afficher_nom("Ibrahim")    

print(""" Exercice 4 - Manipuler des variables globales et locales : Crée une variable globale x, puis une fonction qui affiche sa valeur. Modifie la valeur de x à l'intérieur de la fonction et affiche-la à nouveau.""")

x = 24
def valeur_x():
    global x
    print(x)
    x = x + 1
    print(x)
valeur_x()
print(x)