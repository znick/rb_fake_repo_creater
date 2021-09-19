#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import json

RB_REPOS_PATH = "/var/lib/anytask/repos"


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        repo_id = int(self.path[1:])

        repo_path = os.path.join(RB_REPOS_PATH, str(repo_id))
        created = False
        if not os.path.exists(repo_path):
            os.symlink(RB_REPOS_PATH, repo_path)
            created = True

        reply = {
            "ok": True,
            "created": created,
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(reply))


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('0.0.0.0', 4444), Handler)
    server.serve_forever()


if __name__ == '__main__':
    run()
