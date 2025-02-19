from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 5000
handler = SimpleHTTPRequestHandler
server = HTTPServer(("0.0.0.0", PORT), handler)

print(f"Serving on port {PORT}...")
server.serve_forever()
