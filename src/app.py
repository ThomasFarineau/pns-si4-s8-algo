import argparse
import http.server
import json
import urllib.parse

from algo import best_move
from format import Format
from verification import Verification


def send_detail(detail, status):
    return [status, {'detail': detail}, 'application/json']


def main(port, time):
    def move(b):
        f = Format(b)
        if not f.is_valid():
            return send_detail(f.message, 400)
        v = Verification(f.formatted_board())
        if not v.is_valid():
            return send_detail(v.message, 422)
        return [200, best_move(v.board, time), 'application/json']

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

    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, ServerHandler)
    print('Serveur en écoute sur le port ' + str(port) + ' ...')
    httpd.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments pour le serveur")
    parser.add_argument("-p", "--port", help="Le port", required=False, default=8000, type=int)
    parser.add_argument("-t", "--time", help="Le temps de réflexion", required=False, default=1, type=float)
    args = parser.parse_args()
    main(args.port, args.time)
