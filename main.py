# La cible
import random

def verifie(prix_a_trouver,essai):
    if prix_a_trouver == essai:
        print("Bravo !")
        return 0
    elif prix_a_trouver < essai:
        print("Trop élevé...")
        return 1
    else:
        print("Trop peu...")
        return -1

prix_a_trouver = random.randint(1,10)
print(f"Prix à trouver : {prix_a_trouver}")

for i in range(1, 6):

    # L'essai
    essai = input(f"Essai n°{i} : Votre proposition (entre 1 et 10) : ")
    try:    
        essai = int(essai)
    except ValueError as exeption:
        print("Erreur de saisie...")
        print(f"Message de Python: {exeption}")
        continue
        
    #print(f"Type de prix_a_trouver : {type(prix_a_trouver)}")
    #print(f"Type de essai : {type(essai)}")

    # La comparaison
    if verifie(prix_a_trouver,essai)==0:
        break
    

print("Fin...")