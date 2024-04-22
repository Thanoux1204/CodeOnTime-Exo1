# liste des temps de chaque pays (sous forme de hashmap (java))
tempsPays = {}

# Lecture du fichier
with open('in/data.txt', 'r', encoding='utf-8') as fichier_in:
    # Lecture de chaque ligne du fichier
    for ligne in fichier_in:
        # Séparation de la ligne en fonction des virgules
        valeur = ligne.strip().split(',')
        nom_pays = valeur[1] # 2e valeur de la ligne
        temps = int(valeur[2])  # 3e valeur de la ligne, converti en entier

        # Ajout du temps au total d'un pays
        if nom_pays in tempsPays:
            tempsPays[nom_pays] += temps
        else:
            tempsPays[nom_pays] = temps

# Trier par ordre croissant des temps
chrono_par_pays_trie = sorted(tempsPays.items(), key=lambda x: x[1])
# Trouver le plus petit temps
paysTempsMin, valeurTempsMin = min(tempsPays.items(), key=lambda x: x[1])

# Écriture des résultats dans un fichier output.txt
with open('out/output.txt', 'w', encoding='utf-8') as fichier_out:
    for pays, somme_temps in chrono_par_pays_trie:
        fichier_out.write(f"{pays}: {somme_temps}\n")
        print(f"{pays}: {somme_temps}")

    print(f"\nLe pays avec le plus petit temps est {paysTempsMin} avec un temps total de {valeurTempsMin}s.")