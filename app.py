import json

from flask import Flask, request, Response
import algo

app = Flask(__name__)
port = 5000


@app.route('/move', methods=['GET'])
def move():
    b = request.args.get('b')
    if b is None:
        return send_detail('Paramètre b manquant', 400)
    format_verif = check_format(b)
    if not format_verif.message == "Valide":
        return send_detail(format_verif.message, 400)
    board = parse_board(b)
    board_verif = check_board(board)
    if not board_verif.message == "Valide":
        return send_detail(board_verif.message, 422)
    # TODO: effectuer les opérations nécessaires avec le paramètre b
    print(algo.score(board))
    return send_detail("Opération effectuée avec succès", 200)


# define response object
class CheckMessage:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def check_board(board):
    print_board(board)
    cd = connect_detector(board)
    if cd[0]:
        return CheckMessage("Il y a un puissance 4 ({} {} {})".format(cd[1], cd[2], cd[3]))
    return CheckMessage("Valide")


def connect_detector(board):
    # for each element in the board
    for i in range(6):
        for j in range(7):
            # if it is not empty
            if board[j][i] is not None:
                # check if there is a "connect 4"
                c4 = check_connect(board, j, i)
                if c4[0]:
                    # if there is a "connect 4", return True
                    return [True, c4[1], c4[2], c4[3]]
    return [False, None, None, None]


def check_connect(board, j, i):
    # check if there is a "connect 4" in the column
    if i < 3:
        if board[j][i] == board[j][i + 1] == board[j][i + 2] == board[j][i + 3]:
            return [True, 'col', j, i]
    # check if there is a "connect 4" in the row
    if j < 4:
        if board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i]:
            return [True, 'row', j, i]
    # check if there is a "connect 4" in the diagonal
    if i < 3 and j < 4:
        if board[j][i] == board[j + 1][i + 1] == board[j + 2][i + 2] == board[j + 3][i + 3]:
            return [True, 'diag', j, i]
    # check if there is a "connect 4" in the other diagonal
    if i < 3 and j > 2:
        if board[j][i] == board[j - 1][i + 1] == board[j - 2][i + 2] == board[j - 3][i + 3]:
            return [True, 'diag', j, i]
    return [False, None, None, None]


def check_format(b):
    # check length is 42
    if len(b) != 42:
        return CheckMessage(
            "La chaîne de caractères doit contenir 42 caractères, actuellement {} caractères".format(len(b)))
    # check if only 0, m or h
    for c in b:
        if c not in ['0', 'm', 'h']:
            return CheckMessage("La chaîne de caractères ne doit contenir que des 0, des m ou des h")
    for i in range(7):
        for j in range(6):
            index = i * 6 + j
            # check if there is a 0 before an m or h
            if b[index] != '0' and b[index - 1] == '0' and index % 6 != 0:
                return CheckMessage("Il ne peut pas y avoir de 0 avant un m ou un h dans la même colonne")
    # check if the board is empty
    if b.count('0') == 42:
        return CheckMessage("Valide")
    # check if h = m + 1
    if b.count('h') != b.count('m') + 1:
        return CheckMessage(
            "Il doit y avoir n(h) = n(m) + 1, actuellement n(h) = {} et n(m) = {}".format(b.count('h'), b.count('m')))
    return CheckMessage("Valide")


def send_detail(detail, status):
    return Response(json.dumps({'detail': detail}, ensure_ascii=False), status=status, mimetype='application/json')


def parse_board(b):
    board = []
    col_len = 6
    # split b in 7 columns of 6 chars
    for i in range(0, len(b), col_len):
        col = list(b[i:i + col_len])
        # replace 0 with None
        col = [None if c == '0' else c for c in col]
        col.reverse()
        board.append(col)
    return board


def print_board(board):
    # print the board in a nice way
    # add indicators for columns
    print('•\t0\t1\t2\t3\t4\t5\t6', end='\n')
    for i in range(6):
        # add indicators for columns
        print(i, end='\t')
        for j in range(7):
            # add indicators for rows
            # replace None with •
            if board[j][i] is None:
                print('•', end='\t')
            else:
                print(board[j][i], end='\t')
        print()


if __name__ == '__main__':
    app.run(debug=True, port=port)
