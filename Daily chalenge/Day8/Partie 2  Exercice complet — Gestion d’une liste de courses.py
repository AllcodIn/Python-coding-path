liste_courses = []

menu = ("""
\n1.Ajouter un article
\n2.Supprimer un article
\n3.Afficher la liste
\n4.Vider la liste  
\n5.Quitter le programme  
""")


while True:
    print(menu)
    option = int(input("Choisissez une option: "))
    
    if (option == 1):
        nom_article_ajoute = input("Entrez le(s) nom(s) de l'article ou des articles  a ajouter: ")
        for article in nom_article_ajoute.split(","):
            article = nom_article_ajoute.strip()
        if article:
            liste_courses.append(nom_article_ajoute)
            print(f"Votre liste de courses a ete mise a jour: \n{liste_courses}")

    elif option == 2:
        nom_article_supprime = input("Entrez le nom de l'article a supprimer: ")
        if nom_article_supprime in liste_courses:
            liste_courses.remove(nom_article_supprime)
            print(f"Votre liste de courses a ete mise a jour: \n{liste_courses}")
        else:
            print("Cet article n'est pas dans la liste")

    elif option == "3":
        if liste_courses:
            print("Votre liste de courses :")
            for i, item in enumerate(liste_courses, 1):
                print(f"{i}. {item}")
        else:
            print("La liste est vide.")

    elif option == 4:
        liste_courses.clear()
        print("La liste a ete videe")

    elif option == "5":
        print("Sauvegarde de votre liste dans 'liste_courses.txt'...")
        with open("liste_courses.txt", "w", encoding="utf-8") as fichier:
            for article in liste_courses:
                fichier.write(article + "\n")
        print("Liste sauvegardée. À bientôt !")
        break

    else:
        print("Option invalide. Veuillez entrer un chiffre entre 1 et 5.")
# while(option != 5):
