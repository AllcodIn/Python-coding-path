chaine = "Supercalifragilisticexpialidocious"


print("\n\n1.Affiche toutes les lettres situées à des positions impaires: ")
for i in range(len(chaine)):
    if i % 2 != 0:
        print(f"{chaine[i]} ", end="")

print("\n\n2.Affiche les voyelles uniquement: ")

voyelles = ['a','i','u','e','o','y']
for letter in chaine:
    if letter in voyelles:
        print(letter, end="")

print("\n\n3.Compte combien de fois la lettre 'i' apparaît: ")
# meter = 0 Bonne methode mais il y a encore mieux
# for letter in chaine:
#     if letter == "i":
        # meter +=1
        # print(meter, end="")
print(chaine.count("i")) #celle la

print("\n\n4.Construit une chaîne avec les lettres aux index multiples de 3: ")
for i in range(len(chaine)):
    if i % 3 == 0:
        new_chaine = chaine[i]
        print(f"{new_chaine} ", end="")