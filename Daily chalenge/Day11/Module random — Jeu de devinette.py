import random

nombre_a_deviner = random.randint(1,100)
nbr_tentative = 7
essais = 0
trouve = False

print("Devine le nombre entre 1 et 100! Tu as 7 essais.")
while essais < nbr_tentative and not trouve:
    try:
        jeu = int(input(f"Essai {essais+1}: "))
        essais += 1
        if jeu < nombre_a_deviner:
            print("Trop petit")
        elif jeu > nombre_a_deviner:
            print("Trop grand")
        else:
            print(f"Vous avez trouvez en {essais} essais")
            trouve = True
    except ValueError:
        print("Veuillez entrer un nombre valide")
if not trouve:
            print(f"Tu as perdu, le nombre a devine etait {nombre_a_deviner}")