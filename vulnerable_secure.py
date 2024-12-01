def analyser_nom_securise(chaine_entree):
    if len(chaine_entree) < 2 or len(chaine_entree) > 50:  # Ajout d'une limite maximale
        raise ValueError("Longueur du nom invalide")
    
    parties = chaine_entree.split(" ")
    if len(parties) != 2:
        raise ValueError("Le nom doit comporter exactement deux parties")
        
    prenom, nom = parties
    
    # Transformation sécurisée
    if prenom.startswith("@"):
        transforme = prenom[1:].upper()  # Transformation simple en majuscules
        return f"{transforme} {nom}"
        
    return f"{prenom} {nom}"
