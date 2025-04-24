matrice = [

[1, 2, 3],

[4, 5, 6],

[7, 8, 9]

]

print("\n 1.Affiche l’élément du centre")
print(f"{matrice[1][1]}")

print("\n 2.Affiche la première ligne")
print(f"{matrice[0]}")

print("\n 3.Affiche la dernière colonne")
print(f"{matrice[0][2]},{matrice[1][2]}, {matrice[2][2]}")
# print([ligne[2] for ligne in matrice]) une pepite!!!


print("\n 4.Inverse l’ordre des lignes")
print(f"{matrice[::-1]}")