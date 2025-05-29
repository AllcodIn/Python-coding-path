import random
import string

def generer_mot_de_passe(longueur):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choices(caracteres, k=longueur))
    return mot_de_passe 

def main():
    try:
        nbr_de_mot = int(input("Combien de mots de passe souhaitez vous généré?:"))
        longueur = int(input("Combien de caractères souhaitez vous pour votre mot de passe?: "))
        if longueur < 6:
            print("La longueur minimale recommandee est de 6 caracteres")
            return
        print("Mots de passe générés: ")
        for i in range(nbr_de_mot):
            mot  = generer_mot_de_passe(longueur)
            print(f"{i+1}.{mot}")

    except Exception as e:
        print(f"Error: {e}")

main()