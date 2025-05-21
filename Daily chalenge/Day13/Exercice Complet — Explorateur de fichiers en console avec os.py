import os
print(" Explorateur de fichiers en console avec os \n")

while True:
    try:
        print("\nRepertoire courant: ",os.getcwd())
        rep_cour = os.getcwd()
        print("\n Contenu du repertoire: ")
        for item in os.listdir():
            print(" -", item)

        menu = int(input("""\n

        1 → Changer de répertoire
        2 → Supprimer un fichier
        3 → Créer un dossier
        4 → Revenir au dossier parent
        5 → Quitter

    >"""))
    
    
        if menu == 1:
            redirect = input("Choissez le repertoire ou aller: ")
            os.chdir(redirect)
            if os.path.isdir(redirect):
                
                print(f"Vous etes dans {os.getcwd()}")
            else:
                print("Ce dossier n'existe pas")

        elif menu == 2:
            file_name = input("Entrez le nom du dossier a supprimer: ")
            if os.path.isfile(file_name):

                os.remove(file_name)
            else: 
                print("Ce fichier n'existe pas")

        elif menu == 3:
            new_folder = input("Entrez le nom du dossier que vous souhaitez creer: ")

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
                print("Dossier cree")

            else:
                print("Ce dossier existe deja")


        elif menu == 4:
          os.chdir("..")
          print(f"Vous etes revenu dans {os.getcwd()}")


        elif menu == 5:
            print("A la tafa")
            break
        
        else:
            print("Choix invalide!!! Veuillez entrez un chiffre compris entre 1 et 5")

    except Exception as e:
        print(f" Error : {e}")