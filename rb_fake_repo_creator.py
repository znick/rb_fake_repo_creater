#!/usr/bin/env python3

DEBUG = True
RB_REPOS_PATH = "/var/lib/anytask/repos"

from flask import Flask
from flask import request
app = Flask(__name__)

import json
import os


@app.route('/<int:repo_id>')
def suggest_handler(repo_id):
    repo_path = os.path.join(RB_REPOS_PATH, str(repo_id))
    created = False
    if not os.path.exists(repo_path):
        os.symlink(RB_REPOS_PATH, repo_path)
        created = True

    reply = {
        "ok": True,
        "created": created,
    }
    return json.dumps(found), 200, {'Content-Type': 'text/json'}

if __name__ == '__main__':
    app.run(debug=DEBUG)
