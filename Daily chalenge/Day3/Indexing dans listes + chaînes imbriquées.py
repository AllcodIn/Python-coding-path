mots = ["Bonjour", "tout", "le", "monde"]


print("\n1.Affiche le premier mot")
print(f"\n {mots[0]}")

print("\n2.Affiche la première lettre du dernier mot")
print(f"\n {mots[-1][0]}")

print("\n3.Affiche les 2 dernières lettres du mot 'Bonjour'")
print(f"\n {mots[0][-2:]}")

print("\n4.Affiche 'ou' depuis le mot 'Bonjour' en utilisant l'indexing imbriqué")
print(f"\n {mots[0][4:6]}")