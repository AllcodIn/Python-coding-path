contacts = {}

while True:
    menu = """
    \n1->Ajouter un contact
    \n2->Rechercher un contact
    \n3->Supprimer un contact
    \n4->Afficher tous les contacts
    \n5->Quitter

    """
    option = int(input("\nChoisissez une option: "))

    if option == 1:
        add_nom = input("Entrez le nom de la personne: ")
        add_cont = input("Entrez le contact sous ce format:  xx-xx-xx-xx")
        contacts[f"{add_nom}"] = add_cont
        
        with open('Daily chalenge\Day9\contacts.txt',"a", encoding="utf-8") as file:
            file.write(add_nom +":"+ contacts[f"{add_nom}"] + "\n")
        print("Contact ajoute")

    elif option == 2:
        rech_nom = input("Entrez le nom de la personne dont vous cherche le contact: ")
        if rech_nom in contacts:
            print(rech_nom +":"+ contacts[f"{rech_nom}"])
        else:
            print("\nCette personne ne figure pas dans votre repertoire.")
            chx = input("\nSouhaiter vous l'ajouter?(Oui/Non)")
            if chx == "Oui":
                add_nom = input("Entrez le nom de la personne: ")
                add_cont = input("Entrez le contact sous ce format: xx-xx-xx-xx")
                contacts[f"{add_nom}"] = add_cont
                with open('Daily chalenge\Day9\contacts.txt',"a", encoding="utf-8") as file:
                    file.write(add_nom +":"+ contacts[f"{add_nom}"] + "\n")
                    print("Contact ajoute")
            
            elif chx == "non":
                print("Operation annulee")

            else:
                print("Veuillez choisir entre Oui ou Non s'il vous plait")
    
    elif option == 3:
        supp_nom = input("Entrez le nom de la personne dont vous shouaite supprimer le contact: ")
        if supp_nom in contacts:
            del contacts[supp_nom]
            print("Contact supprime")
        else:
            print("Contact inexistant dans votre repertoire")
            chx = input("\nSouhaiter vous l'ajouter?(Oui/Non)")
            if chx == "Oui":
                add_nom = input("Entrez le nom de la personne: ")
                add_cont = input("Entrez le contact sous ce format: xx-xx-xx-xx")
                contacts[f"{add_nom}"] = add_cont
                with open('Daily chalenge\Day9\contacts.txt',"a", encoding="utf-8") as file:
                    file.write(add_nom +":"+ contacts[f"{add_nom}"] + "\n")
                    print("Contact ajoute")
            elif chx == "non":
                print("Operation annulee")

            else:
                print("Veuillez choisir entre Oui ou Non s'il vous plait")

    elif option == 4:
        for i, items in enumerate(contacts, 1):
            print(f"{i}.{items}")

        with open('Daily chalenge\Day9\contacts.txt',"r", encoding="utf-8") as file:
            print("Aucun contact enregistre")
            chx = input("\nSouhaiter vous l'ajouter?(Oui/Non)")
            if chx == "Oui":
                add_nom = input("Entrez le nom de la personne: ")
                add_cont = input("Entrez le contact sous ce format: xx-xx-xx-xx")
                contacts[f"{add_nom}"] = add_cont
                with open('Daily chalenge\Day9\contacts.txt',"a", encoding="utf-8") as file:
                    file.write(add_nom +":"+ contacts[f"{add_nom}"] + "\n")
                    print("Contact ajoute")
            elif chx == "non":
                print("Operation annulee")

            else:
                print("Veuillez choisir entre Oui ou Non s'il vous plait")

    
    elif option == 5:
        print("Fermeture du programme...")
        break

