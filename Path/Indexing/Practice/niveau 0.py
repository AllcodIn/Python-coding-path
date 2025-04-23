mot = "Python"

print("\n Afficher la première lettre du mot : ")
q1 = mot[0]
print(f"{q1} \n")

print("\n Afficher la deuxième lettre : ")
q2 = mot[1]
print(f"{q2} \n")

print("\n Afficher la dernière lettre : ")
q3 = mot[-1]
print(f"{q3} \n")

print("\n Afficher les trois premières lettres : ")
q4 = mot[0:3]
print(f"{q4} \n")

print("\n Afficher les trois dernières lettres : ")
q5 = mot[-3:]
print(f"{q5} \n")

print("\n Afficher le mot en ordre inversé : ")
q6 = mot[::-1]
print(f"{q6} \n")

print("\n Afficher uniquement les lettres y, t, o (avec les index) : ")
q7 = {mot[1], mot[2], mot[4]}
print(f"{q7} \n")
print(mot[1], mot[2], mot[4])
