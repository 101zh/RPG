from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import socket
from tic_tac_toe import processData


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
        return

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        # passed in data from the front end
        # {'playerName': 'hunter', 'result': 'win'}
        data = json.loads(post_body)
        print(data)

        # Todo: define function in another python file
        # [{"name":"Hunter", "score":"1"}, {"name":"Hunter2", "score":"0"}]
        # {"Hunter": 1, "Hunter2": 0}
        #response_data =process_swin_loss_tie(data)

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # response to the front end
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version,
            'body': processData(data)
        }).encode())
        return

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


if __name__ == '__main__':
    print('localhost', 'ip', socket.gethostbyname(socket.gethostname()))
    server = HTTPServer(('localhost', 8000), RequestHandler)
    print('Starting server at http://localhost:8000')
    server.serve_forever()
