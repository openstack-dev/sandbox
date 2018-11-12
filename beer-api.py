from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
	self.wfile.write("<html><body><h1>BEER!</h1></body></html>")

PORT = 8000

httpd = SocketServer.TCPServer(("", PORT), S)

print "serving at port", PORT
httpd.serve_forever()

