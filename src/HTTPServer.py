import json
from http.server import BaseHTTPRequestHandler, HTTPServer  # python3
from io import BytesIO


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        output = json.loads(body.decode('utf-8'))

        # result = tryToAddForm(output)


        response.write(body)
        self.wfile.write(response.getvalue())
        print(output)

    # def do_PUT(self):
    #     self.do_POST()


host = ''
port = 8080
HTTPServer((host, port), HandleRequests).serve_forever()

