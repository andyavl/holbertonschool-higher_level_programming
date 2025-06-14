#!/usr/bin/python3
"""
Simple HTTP API Server using Python's built-in http.server module.

This server responds to GET requests at specific endpoints:
- /data   → returns sample JSON data
- /status → returns plain text OK
- /info   → returns API metadata in JSON format
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler class for handling basic API GET endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests to specific API endpoints.
        Responds with JSON or plain text depending on the requested path.
        """

        if self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Simple API root')

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def runserver(server=HTTPServer, handler=SimpleAPIHandler, port=8000):
    """
    Starts the HTTP server on the specified port with the given handler.

    Args:
        server: HTTP server class to use (default: HTTPServer)
        handler: Request handler class to use (default: SimpleAPIHandler)
        port (int): Port number to bind the server to (default: 8000)
    """
    tcp_address = ('', port)
    httpd = server(tcp_address, handler)
    print(f"Server running at http://localhost:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    runserver()
