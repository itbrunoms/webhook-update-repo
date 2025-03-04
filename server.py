rom http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

class GitPullHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/gitpull':
            try:
                # change to you repository folder
                repo_path = '/'

                process = subprocess.Popen(['git', 'pull'], cwd=repo_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
              
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(stdout)

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            self.send_response(404)
            self.end_headers()

#default por is 8001
def run(server_class=HTTPServer, handler_class=GitPullHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
