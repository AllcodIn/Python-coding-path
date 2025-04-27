article1 = "Playstation5 Pro"
article2 = "Alienware"
article3 = "NVIDIA RTX 5090"

prix_article1 =  500
prix_article2 = 800
prix_article3 = 455

quantite_article1 = 10
quantite_article2 = 8 
quantite_article3 = 7

total_article1 = prix_article1 * quantite_article1
total_article2 = prix_article2 * quantite_article2
total_article3 = prix_article3 * quantite_article3

total_panier = total_article1 + total_article2 + total_article3

remise = 0.1

print(f""" \n
{article1}
\tPrix unitaire: {prix_article1}
\tquantite {quantite_article1}
\ttotal: {total_article1}

{article2}
\tPrix unitaire: {prix_article2}
\tquantite {quantite_article2}
\ttotal: {total_article2}

{article3}
\tPrix unitaire: {prix_article3}
\tquantite {quantite_article3}
\ttotal: {total_article3}

Total general: {total_panier}

Prix du panier apres remise: {total_panier*remise}
""")