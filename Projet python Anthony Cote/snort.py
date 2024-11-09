# Crée un plateau de jeu de taille n x n
def newBoard(n):
    board = []
    for i in range(n):
        board.append([0] * n)
    return board

# Affiche le plateau de jeu dans la console
def displayBoard(board, n):
    for i in range(n):
        print(i + 1, '|', end=' ')
        for j in range(n):
            if board[i][j] == 0:
                print('.', end=' ')
            elif board[i][j] == 1:
                print('X', end=' ')
            elif board[i][j] == 2:
                print('o', end=' ')
        print('')
    
    print('   ', end='')
    for _ in range(n * 2):
        print('_', end='')
    print('\n   ', end='')
    for i in range(1, n + 1):
        print(i, end=' ')
    print('\n')

# Vérifie si la case (i, j) est jouable pour le joueur
def possibleSquare(board, n, player, i, j):
    if board[i][j] != 0:
        return False

    opponent = 2 if player == 1 else 1

    if ((i > 0 and board[i - 1][j] == opponent) or
        (i < n - 1 and board[i + 1][j] == opponent) or
        (j > 0 and board[i][j - 1] == opponent) or
        (j < n - 1 and board[i][j + 1] == opponent)):
        return False

    return True

# Demande au joueur de saisir des coordonnées valides pour poser un pion
def selectSquare(board, n, player):
    while True:
        print(f'Joueur {player}, à toi de jouer !')

        ligne = input('Quelle ligne ? ')
        while not ligne.isnumeric() or int(ligne) == 0 or int(ligne) > n:
            print('Numéro de ligne incorrecte, veuillez entrer un nombre entier entre 1 et', n)
            ligne = input('Quelle ligne ? ')
        i = int(ligne) - 1

        colonne = input('Quelle colonne ? ')
        while not colonne.isnumeric() or int(colonne) == 0 or int(colonne) > n:
            print('Numéro de colonne incorrect, veuillez entrer un nombre entier entre 1 et', n)
            colonne = input('Quelle colonne ? ')
        j = int(colonne) - 1

        if possibleSquare(board, n, player, i, j):
            return i, j
        else:
            print('Vous ne pouvez pas placer un pion ici.')

# Met à jour le plateau avec le coup du joueur
def updateBoard(board, player, i, j):
    board[i][j] = player

# Vérifie s'il reste des coups possibles pour le joueur
def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if possibleSquare(board, n, player, i, j):
                return True
    return False

# Fonction principale du jeu
def snort(n):
    board = newBoard(n)
    player = 1

    while again(board, n, player):
        displayBoard(board, n)
        i, j = selectSquare(board, n, player)
        updateBoard(board, player, i, j)
        player = 2 if player == 1 else 1
    print(f'\nLe joueur {2 if player == 1 else 1} a gagné !')
    displayBoard(board, n)

# Demande la taille du plateau et lance le jeu
taille = input('Quelle taille de plateau ? ')

while not taille.isnumeric() or int(taille) == 0:
    print('Taille de plateau incorrecte, veuillez entrer un entier supérieur à 0.')
    taille = input('Quelle taille de plateau ? ')

snort(int(taille))