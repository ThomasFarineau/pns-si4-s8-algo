import http.server
import urllib.parse
import json

from algo import best_move
from format import Format
from verification import Verification


def move(b):
    f = Format(b)
    if not f.is_valid():
        return send_detail(f.message, 400)
    v = Verification(f.formatted_board())
    if not v.is_valid():
        return send_detail(v.message, 422)
    return [200, best_move(v.board, 1), 'application/json']


def send_detail(detail, status):
    return [status, {'detail': detail}, 'application/json']


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        if parsed_path.path == '/move' and 'b' in query_params:
            m = move(query_params['b'][0])
            json_to_send = json.dumps(m[1])
            # Traiter la requête ici
            self.send_response(m[0])
            self.send_header('Content-type', m[2])
            self.end_headers()
            self.wfile.write(json_to_send.encode("utf-8"))
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
