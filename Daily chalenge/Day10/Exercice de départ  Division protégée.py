numerateur = int(input("Entrez le numerateur: "))
denominateur = int(input("Entrez le denominateur: "))
quotien = numerateur/denominateur

try:
    print(f"\nLe quotient de {numerateur} par {denominateur} est: {quotien}")
    
except ZeroDivisionError:
    print("La division d'un nombre par zero n'est pas possible ")
finally:
    print("\n fin du programme")