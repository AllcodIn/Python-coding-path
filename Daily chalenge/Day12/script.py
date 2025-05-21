import sys

if len(sys.argv) < 3:
    print("Erreur: Veuillez fournir un nom et un age")
else:
    name = sys.argv[1]
    age = sys.argv[2]

print(f"Hello {name}, you are {age} years old")