# EV 2 - Conditions
# Exercice 2 : Bonjour !
genre = input("Civilité : (Homme/Femme/Indéfini) : ")
age = int(input("Age : "))

if genre == "Homme":
    print("Bonjour Monsieur !")
elif genre == "Femme":
    if age > 18:
        print("Bonjour Madame !")
    else:
        print("Bonjour Mademoiselle !")
else :
    print("Bonjour !")