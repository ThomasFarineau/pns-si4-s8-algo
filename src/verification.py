class Verification:
    def __init__(self, board):
        self.board = board
        self.message = None

    def is_valid(self):
        # On vérifie que le board ne contient pas de puissance 4.
        e = self.is_ended()
        if e[0]:
            self.message = "Le plateau contient une puissance 4, le joueur {} a gagne avec {}.".format(e[1], e[2])
            return False
        # On vérifie que la board n’est pas pleine.
        if self.is_full():
            self.message = "Le plateau est plein"
            return False
        return True

    def is_full(self):
        for i in range(6):
            for j in range(7):
                if self.board[j][i] is None:
                    return False
        return True

    def is_ended(self):
        # Pour chaque élément du board
        for i in range(7):
            for j in range(6):
                # Si l’élément est un "h" ou un "m".
                if self.board[i][j] is not None:
                    # On vérifie s’il y a un "puissance 4".
                    p4 = self.is_connect(i, j)
                    if p4[0]:
                        # S’il y a une puissance 4, on retourne True
                        return [True, self.board[i][j], p4[1]]
        return [False, None, None]

    def is_connect(self, i, j):
        # On vérifie s’il y a un "puissance 4" dans la colonne
        if j < 3:
            if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                return [True, [[i, j], [i, j + 1], [i, j + 2], [i, j + 3]]]
        # On vérifie s’il y a un "puissance 4" dans la ligne
        if i < 4:
            if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                return [True, [[i, j], [i + 1, j], [i + 2, j], [i + 3, j]]]
        # On vérifie s’il y a un "puissance 4" dans la diagonale
        if i < 4 and j < 3:
            if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                return [True, [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]]]
        # On vérifie s’il y a un "puissance 4" dans l’autre diagonale
        if i > 2 and j < 3:
            if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3]:
                return [True, [[i, j], [i - 1, j + 1], [i - 2, j + 2], [i - 3, j + 3]]]
        return [False, None]
