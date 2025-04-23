from tkinter import Tk, filedialog
import os
import platform

# Masquer la fenêtre principale Tkinter
Tk().withdraw()

# Ouvrir la fenêtre de sélection de fichier
chemin_fichier = filedialog.askopenfilename(
    title="Choisis un fichier à ouvrir",
    filetypes=[("Tous les fichiers", "*.*")]
)

# Vérifie si un fichier a été sélectionné
if chemin_fichier:
    print(f"📄 Fichier sélectionné : {chemin_fichier}")

    # Ouvre le fichier avec l'application par défaut selon l'OS
    if platform.system() == "Windows":
        os.startfile(chemin_fichier)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open '{chemin_fichier}'")
    else:  # Linux
        os.system(f"xdg-open '{chemin_fichier}'")
else:
    print("⚠️ Aucun fichier sélectionné.")
