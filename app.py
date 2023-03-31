from flask import Flask, request, jsonify

app = Flask(__name__)
port = 5000


@app.route('/move', methods=['GET'])
def move():
    b = request.args.get('b')
    if b is None:
        return send_detail('Paramètre b manquant', 400)
    check = check_format(b)
    if not check[0]:
        return send_detail(check[1], 400)
    # TODO: effectuer les opérations nécessaires avec le paramètre b
    print_board(parse_board(b))
    result = {'message': 'Opération effectuée avec succès'}
    return jsonify(result)


def check_format(b):
    # check length is 42
    if len(b) != 42:
        return False, "La chaîne de caractères doit contenir 42 caractères"
    # check if only 0, m or h
    for c in b:
        if c not in ['0', 'm', 'h']:
            return False, "La chaîne de caractères ne doit contenir que des 0, des m ou des h"
    for i in range(7):
        for j in range(6):
            index = i * 6 + j
            # check if there is a 0 before an m or h
            if b[index] != '0' and b[index - 1] == '0' and index % 6 != 0:
                return False, "Il ne peut pas y avoir de 0 avant un m ou un h dans la même colonne"
    # check if h = m + 1
    if b.count('h') != b.count('m') + 1:
        return False, "Il doit y avoir n(h) = n(m) + 1"
    return True, "Oui"


def send_detail(detail, status):
    return jsonify({'detail': detail}), status


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
