from flask import Flask, request, jsonify

app = Flask(__name__)
port = 5000


@app.route('/move', methods=['GET'])
def move():
    b = request.args.get('b')
    if b is None:
        return send_detail('Paramètre b manquant', 400)
    if not is_valid(b):
        return send_detail('Paramètre b invalide', 400)
    # TODO: effectuer les opérations nécessaires avec le paramètre b
    print(parse_board(b))
    result = {'message': 'Opération effectuée avec succès'}
    return jsonify(result)


def is_valid(b):
    # check length is 42
    if len(b) != 42:
        return False
    # check if only 0, m or h
    for c in b:
        if c not in ['0', 'm', 'h']:
            return False
    return True


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


if __name__ == '__main__':
    app.run(debug=True, port=port)
