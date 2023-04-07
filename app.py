import json

from flask import Flask, request, Response
from format import Format, print_board
from verification import Verification

app = Flask(__name__)
port = 5000


@app.route('/move', methods=['GET'])
def move():
    b = request.args.get('b')
    f = Format(b)
    if not f.is_valid():
        return send_detail(f.message, 400)
    v = Verification(f.formatted_board())
    if not v.is_valid():
        return send_detail(v.message, 422)

    board = v.board
    print_board(board)

    # TODO: effectuer les opérations nécessaires avec le paramètre b
    # print(algo.score(board))
    return send_detail("Opération effectuée avec succès", 200)


def send_detail(detail, status):
    return Response(json.dumps({'detail': detail}, ensure_ascii=False), status=status, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=port)
