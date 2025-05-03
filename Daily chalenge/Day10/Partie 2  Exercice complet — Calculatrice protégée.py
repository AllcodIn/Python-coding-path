n1 = float(input("Entrez un premier nombre: "))
n2 = float(input("Entrez un second nombre: "))

while True:

    menu = (input("""
        Quelle operation souhaitez vous effectuer(+,-,*,/?: """))


    if menu == "+":
        try:
            print(f"{n1} + {n2} = {n1 + n2}")
        except ValueError:
            print("Veuillez entrer un nombre au lieu d'une lettre s'il vous plait")
        except ValueError:
            print("Operation invalide")
        finally:
            print("Merci d'avoir utilise la calculatrice")
    elif menu == "-":
        try:
            print(f"{n1} - {n2} = {n1 - n2}")
        except ValueError:
            print("Veuillez entrer un nombre au lieu d'une lettre s'il vous plait")
        except ValueError:
            print("Operation invalide")
        finally:
            print("Merci d'avoir utilise la calculatrice")
    elif menu == "*":
        try:
            print(f"{n1} * {n2} = {n1 * n2}")
        except ValueError:
            print("Veuillez entrer un nombre au lieu d'une lettre s'il vous plait")
        except ValueError:
            print("Operation invalide")
        finally:
            print("Merci d'avoir utilise la calculatrice")
    elif menu == "/":
        try:
            print(f"{n1} / {n2} = {n1 / n2}")
        except ValueError:
            print("Veuillez entrer un nombre au lieu d'une lettre s'il vous plait")
        except ZeroDivisionError:
            print("La division d'un nombre par zero n'est pas possible")
        except ValueError:
            print("Operation invalide")
        finally:
            print("Merci d'avoir utilise la calculatrice")
        break