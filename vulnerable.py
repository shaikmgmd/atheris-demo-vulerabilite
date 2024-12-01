# vulnerable.py
def analyser_nom(chaine_entree):
    if len(chaine_entree) < 2:
        raise ValueError("Nom trop court")
    
    parties = chaine_entree.split(" ")
    if len(parties) != 2:
        raise ValueError("Le nom doit comporter exactement deux parties")
        
    prenom, nom = parties
    
    if prenom.startswith("@"):
        transforme = eval(prenom[1:])
        return f"{transforme} {nom}"
        
    return f"{prenom} {nom}"
    
print(analyser_nom("Emmanuel Macron")) # -> "Emmanuel Macron"
print(analyser_nom("Hashif Batcha")) # -> "Hashif Batcha"
print(analyser_nom('@__import__("os").system("ls") Nadifi'))
#print(analyser_nom("@Mbahal Mbappe")) # -> ?
