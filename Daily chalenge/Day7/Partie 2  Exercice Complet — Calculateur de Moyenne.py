print("Entrez vos trois notes")

note1 = float(input("\nEntrez la note 1: "))
note2 = float(input("\nEntrez la note 2: "))
note3 = float(input("\nEntrez la note 3: "))

def calculer_moyenne(n1, n2, n3):
    global note1
    global note2
    global note3

    n1 = note1
    n2 = note2
    n3 = note3

    moyenne = (n1 + n2 + n3)/3
    return moyenne

def afficher_resultat(moyenne):
    if(moyenne >= 16):
        print("Tres bien")
    elif(moyenne >= 14):
        print("Bien")
    elif(moyenne >= 10):
        print("Passable")
    else:
        print("Vous n'avez pas echoue, vous etes en train de reussir")
print(calculer_moyenne(note1,note2,note3))

resultat = calculer_moyenne(note1,note2,note3)
afficher_resultat(resultat)