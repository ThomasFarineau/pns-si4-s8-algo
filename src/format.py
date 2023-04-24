def print_board(board):
    # On met les indices des colonnes
    print('•\t0\t1\t2\t3\t4\t5\t6', end='\n')
    for i in range(6):
        # On met les indices des lignes
        print(i, end='\t')
        for j in range(7):
            # on remplace les "None" par des "•".
            if board[j][i] is None:
                print('•', end='\t')
            else:
                print(board[j][i], end='\t')
        print()


class Format:
    def __init__(self, board):
        self.board = board
        self.message = None

    def is_valid(self):
        # On vérifie que le board est bien présent
        if self.board is None:
            self.message = "Parametre b manquant"
            return False
        # On vérifie que le board est bien une chaîne de caractères de 42 caractères
        if len(self.board) != 42:
            self.message = "La chaine de caracteres doit contenir 42 caracteres, actuellement {} caracteres".format(
                len(self.board))
            return False
        # On vérifie que le board ne contient que des 0, des m ou des h.
        for c in self.board:
            if c not in ['0', 'm', 'h']:
                self.message = "La chaine de caracteres ne doit contenir que des 0, des m ou des h"
                return False
        # On vérifie que le board ne contient pas de 0 avant un m ou un h dans la même colonne
        if not self.valid_placement():
            self.message = "Il ne peut pas y avoir de 0 avant un m ou un h dans la meme colonne"
            return False
        # On vérifie que le nombre de H est égal au nombre de M (ou +1 si l’ordinateur commence).
        if not self.valid_count():
            self.message = "Le nombre de H doit etre egal au nombre de M (ou n(M)+1)"
            return False
        return True

    def formatted_board(self):
        board = []
        col_len = 6
        # On sépare la chaîne de caractères en colonnes de 7 caractères
        for i in range(0, len(self.board), col_len):
            col = list(self.board[i:i + col_len])
            # On remplace tous les 0 par None pour faciliter la manipulation du board
            col = [None if c == '0' else c for c in col]
            # On inverse la colonne pour faciliter la manipulation du board
            col.reverse()
            board.append(col)
        return board

    def valid_count(self):
        ch = self.board.count('h')
        cm = self.board.count('m')
        diff = ch - cm
        if diff != 0 and diff != 1:
            return False
        return True

    def valid_placement(self):
        for i in range(7):
            for j in range(6):
                index = i * 6 + j
                if self.board[index] != '0' and self.board[index - 1] == '0' and index % 6 != 0:
                    return False
        return True
