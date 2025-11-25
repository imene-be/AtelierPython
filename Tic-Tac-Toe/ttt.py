import random

def afficher_grille(grille):
    print()
    for i in range(3):
        print(" | ".join(grille[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def verifier_victoire(grille, joueur):
    combinaisons = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(grille[i] == joueur for i in combi) for combi in combinaisons)

def coup_gagnant(grille, joueur):
    """Retourne un coup gagnant si possible, sinon None"""
    for i in range(9):
        if grille[i] not in ["X","O"]:
            copie = grille[:]
            copie[i] = joueur
            if verifier_victoire(copie, joueur):
                return i
    return None

def ia_coup(grille):
    joueur = "X"
    ia = "O"

    # gagne si possible
    gagnant = coup_gagnant(grille, ia)
    if gagnant is not None:
        return gagnant

    # bloque un coup gagnant du joueur
    bloquer = coup_gagnant(grille, joueur)
    if bloquer is not None:
        return bloquer

    # Prendre le centre
    if grille[4] not in ["X", "O"]:
        return 4

    # Prendre un coin
    coins = [0, 2, 6, 8]
    coins_libres = [c for c in coins if grille[c] not in ["X", "O"]]
    if coins_libres:
        return random.choice(coins_libres)

    # Sinon un coup libre
    libres = [i for i, v in enumerate(grille) if v not in ["X","O"]]
    return random.choice(libres)

def tic_tac_toe():
    grille = [str(i+1) for i in range(9)]
    joueur = "X"
    ia = "O"

    afficher_grille(grille)

    for _ in range(9):
        if joueur == "X":
            coup = input("Choisis une case (1-9) : ")
            while not coup.isdigit() or int(coup) not in range(1,10) or grille[int(coup)-1] in ["X","O"]:
                coup = input("Case invalide il faut choisir une case libre (1-9) : ")
            grille[int(coup)-1] = joueur
        else:
            print("L'IA joue...")
            grille[ia_coup(grille)] = ia

        afficher_grille(grille)

        if verifier_victoire(grille, joueur):
            print("Félicitations ! Tu as gagné !" if joueur == "X" else "L'ia a gagné !")
            return

        joueur = ia if joueur == "X" else "X"

    print("Match nul !")

tic_tac_toe()
