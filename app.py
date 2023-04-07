import http.server
import urllib.parse

from format import print_board, Format
from verification import Verification


def move(b):
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
    return [status, {'detail': detail}, 'application/json']


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        if parsed_path.path == '/move' and 'b' in query_params:
            m = move(query_params['b'][0])
            print(m)
            # Traiter la requête ici
            self.send_response(m[0])
            self.send_header('Content-type', m[2])
            self.end_headers()
            self.wfile.write(bytes(m[1]['detail'], 'utf-8'))
        else:
            # Renvoyer une réponse 404 Not Found pour toute autre requête
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')


server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, ServerHandler)

if __name__ == '__main__':
    print('Serveur en écoute sur le port 8000...')
    httpd.serve_forever()
