directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def newBoard(n):
    # Crée un plateau de taille n x n initialisé avec 0.
    # Les pions du joueur 2 sont placés dans la première colonne.
    # Les pions du joueur 1 sont placés dans la dernière ligne (à partir de la colonne 1).
    board = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        board[i][0] = 2  
    for j in range(1, n):
        board[n - 1][j] = 1  
    return board

def displayBoard(board, n):
    # Affiche le plateau de jeu.
    # Utilise 'o' pour les pions du joueur 1, 'x' pour les pions du joueur 2, et '.' pour les cases vides.
    for i in range(n):
        ligne = []
        for j in range(n):
            if board[i][j] == 1:
                ligne.append("o")
            elif board[i][j] == 2:
                ligne.append("x")
            else:
                ligne.append(".")
        print(f"{i + 1} | " + " ".join(ligne))
    print("   " + "___" * n)
    print("   " + "  ".join(str(col + 1) for col in range(n)))
    print('Les pions du joueur 1 sont les o')
    print('Les pions du joueur 2 sont les x')

def saisie_taille_plateau():
    # Demande à l'utilisateur la taille du plateau et valide l'entrée.
    taille = input("Quelle taille de plateau ? ")
    while not taille.isdigit() or int(taille) < 2:
        print("Taille de plateau incorrecte, veuillez entrer un entier supérieur ou égal à 2.")
        taille = input("Quelle taille de plateau ? ")
    return int(taille)

def saisie_position(utilisateur, limite, type_position):
    # Demande à l'utilisateur de saisir une position (ligne ou colonne) et valide l'entrée.
    value = input(utilisateur)
    while not value.isdigit() or not (1 <= int(value) <= limite):
        print(f"Numéro de {type_position} incorrecte, veuillez entrer un nombre entier entre 1 et {limite}.")
        value = input(utilisateur)
    return int(value) - 1  # Retourne l'index (0 basé)

def possiblePawn(board, n, directions, player, i, j):
    if 0 <= i < n and 0 <= j < n and board[i][j] == player:
        # Cas où le joueur 1 peut sortir directement par le haut.
        if player == 1 and i == 0:
            return True
        # Cas où le joueur 2 peut sortir directement par la droite.
        if player == 2 and j == n - 1:
            return True
        for di, direct_j in directions:
            n_vers_i, n_vers_j = i + di, j + direct_j
            if 0 <= n_vers_i < n and 0 <= n_vers_j < n and board[n_vers_i][n_vers_j] == 0:
                return True
    return False


def selectPawn(board, n, directions, player):
    # Demande à l'utilisateur de choisir un pion à déplacer.
    # Vérifie que le pion peut se déplacer.
    while True:
        i = saisie_position('Quelle ligne ? ', n, 'ligne')
        j = saisie_position('Quelle colonne ? ', n, 'colonne')
        if possiblePawn(board, n, directions, player, i, j):
            return i, j
        else:
            print("Saisie impossible. Veuillez choisir un pion qui peut se déplacer.")

def possibleMove(board, n, directions, player, i, j, m):
    di, direct_j = directions[m]
    n_vers_i, n_vers_j = i + di, j + direct_j

    # Cas où le joueur 1 peut sortir sur la première ligne (n_vers_i < 0)
    if player == 1 and n_vers_i < 0:
        return True

    # Cas où le joueur 2 peut sortir sur la dern_vers_ière colonne (n_vers_j >= n).
    if player == 2 and n_vers_j >= n:
        return True
    return 0 <= n_vers_i < n and 0 <= n_vers_j < n and board[n_vers_i][n_vers_j] == 0


def selectMove(board, n, directions, player, i, j):
    # Demande au joueur de choisir une direction pour déplacer son pion.
    if player == 1:
        noms_directions = ["haut", "droite", "gauche"]
    else:
        noms_directions = ["droite", "haut", "bas"]

    while True:
        direction = input(f"Joueur {player}, choisissez la direction ({', '.join(noms_directions)}) : ")
        if direction in noms_directions:
            m = noms_directions.index(direction)
            if possibleMove(board, n, directions, player, i, j, m):
                return m
            else:
                print(f"Déplacement impossible pour le joueur {player} dans cette direction.")
        else:
            print("Direction invalide.")

def move(board, n, directions, player, i, j, m):
    # Effectue le mouvement du pion du joueur.
    di, direct_j = directions[m]
    n_vers_i, n_vers_j = i + di, j + direct_j
    # Sortie pour le joueur 1.
    if player == 1 and n_vers_i < 0:  
        board[i][j] = 0  # Le pion sort du plateau.
        return
    # Sortie pour le joueur 2.
    if player == 2 and n_vers_j >= n:  
        board[i][j] = 0  
        return
    if 0 <= n_vers_i < n and 0 <= n_vers_j < n:
        board[i][j] = 0
        board[n_vers_i][n_vers_j] = player

def bloquer(board, n, directions, player):
    # Vérifie si l'adversaire est bloqué et ne peut plus jouer.
    adversaire = 2 if player == 1 else 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == adversaire:  # Vérifie les pions de l'adversaire.
                if possiblePawn(board, n, directions, adversaire, i, j):
                    return False  
    return True  # L'adversaire est bloqué.

def win(board,directions, n, player):
    # Vérifie si tous les pions du joueur sont sortis.
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                return False
    return True

def dodgem(n):
    # Fonction principale pour exécuter le jeu Dodgem.
    directions_joueur1 = ((-1, 0), (0, 1), (0, -1))  # haut, droite, gauche
    directions_joueur2 = ((0, 1), (-1, 0), (1, 0))  # droite, haut, bas
    board = newBoard(n)
    player = 1

    while True:
        directions = directions_joueur1 if player == 1 else directions_joueur2
        
        # Vérification de victoire avant de permettre au joueur de jouer.
        if win(board,directions, n, 1):  # Vérifie si le joueur 1 a gagné.
            print("Le joueur 1 a fait sortir tous ses pions et a gagné !")
            break
        if win(board,directions, n, 2):  # Vérifie si le joueur 2 a gagné.
            print("Le joueur 2 a fait sortir tous ses pions et a gagné !")
            break
        
        if bloquer(board, n, directions, 1):  # Vérifie si le joueur 1 a bloqué le joueur 2.
            print("Le joueur 1 a bloqué tous les pions de son adversaire et a gagné !")
            break
        if bloquer(board, n, directions, 2):  # Vérifie si le joueur 2 a bloqué le joueur 1.
            print("Le joueur 2 a bloqué tous les pions de son adversaire et a gagné !")
            break

        print(f"joueur {player}, à toi de jouer !")
        displayBoard(board, n)

        # Sélection du pion et du mouvement.
        i, j = selectPawn(board, n, directions, player)
        m = selectMove(board, n, directions, player, i, j)
        move(board, n, directions, player, i, j, m)
        player = 2 if player == 1 else 1

taille = saisie_taille_plateau()
dodgem(taille)