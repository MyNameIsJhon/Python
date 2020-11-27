annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
retour  = False

if annee % 4 != 0 :
    retour = False
elif annee % 100 != 0:
    retour = False
elif annee % 400 != 0:
    retour = False
else :
    retour = True

if retour == True :
    print("c'est une année bissextile")
else :
    print("ce n'est pas une annè bissextile")


