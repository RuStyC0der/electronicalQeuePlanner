import json
from http.server import BaseHTTPRequestHandler, HTTPServer  # python3
from io import BytesIO

from src.databaseConnector import DataBaseConnection
from src.queueManager import QueueAdd


class HandleRequests(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server, *args, **kwargs):
        dbm = DataBaseConnection()
        self.qm = QueueAdd(dbm)
        super().__init__(request, client_address, server)


    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b"received get request")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        try:
            output = json.loads(body.decode('utf-8'))
            result = self.qm.tryToAddForm(output)
            byte_result = json.dumps(result)
            response.write(byte_result.encode())
            print(output)
            print(result)
        except Exception as e:
            errorJSON = {"error": str(e)}
            byte_result = json.dumps(errorJSON)
            response.write(byte_result.encode())

        self.wfile.write(response.getvalue())

    # def do_PUT(self):
    #     self.do_POST()



if __name__ == '__main__':
    host = ''
    port = 8080

    HTTPServer((host, port), HandleRequests).serve_forever()

