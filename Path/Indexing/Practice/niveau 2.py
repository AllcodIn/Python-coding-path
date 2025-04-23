mot = "programmation"

print("\n 1.	Affiche un caractère sur deux")
print(f"\n {mot[1::2]}")

print("\n 2.	Affiche les lettres aux index pairs")
print(f"\n {mot[::2]}")

print("\n 3.	Inverse le mot")
print(f"\n {mot[::-1]}")

print("\n 4.	Affiche les 5 premiers caractères, en inversé")
print(f"\n {mot[:5][::-1]}")