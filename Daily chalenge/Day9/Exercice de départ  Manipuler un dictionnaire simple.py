livre = {
    "titre": "Tomorrow will be an other day",
    "auteurs": "TRAORE Ibrahim Khalil & TRAORE Cheick Abdoul Rachid",
    "annee":2023
}

print(livre["titre"])
livre["page"] = 911
livre["annee"] = 2025
del livre["page"]
print(livre.keys())
print(livre.values())
