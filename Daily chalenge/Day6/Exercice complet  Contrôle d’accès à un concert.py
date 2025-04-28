age = int(input("Entrez votre age s'il vous plait"))

if( age < 5):
    print("Désolé, trop jeune pour entrer")
elif( age < 0):
   print("Age invalide")
elif( age > 120):
   print("Age invalide")
elif( age < 12):
   print("Entree gratuite")
elif( age > 12 and age < 17):
   print("Demi tarif 1250")
elif( age < 18):
   print("Plein tarif 2500")
elif( age < 60):
   print("Tarif reduit senior 1500")
