# EV 2 - Conditions
# Exercice 1 : Mention => correction la plus optimisée (bien que l'alternative complexe n'était pas obligatoire)
note = int(input("Saisissez une note : "))

mention = ""

if note >= 0 and note <= 20:
    # if note >= 12 and note < 14:
    #     mention = "Assez bien"
    # elif note >= 14 and note < 16:
    #     mention = "Bien"
    # elif note >= 16 and note < 18:
    #     mention = "Très bien"
    # elif note >= 18 and note < 20:
    #     mention = "Excellent"
    # elif note == 20:
    #     mention = "Parfait"

    # Autre méthode
    if note == 20:
        mention = "Parfait"
    elif note >= 18:
        mention = "Excellent"
    elif note >= 16:
        mention = "Très bien"
    elif note >= 14:
        mention = "Bien"
    elif note >= 12:
        mention = "Assez bien"

    print(f"Votre note est de {note}/20 {mention}")
else :
    print("Note invalide")