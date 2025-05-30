import os
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

OAUTH_SERVER_URL = os.environ.get('OAUTH_SERVER_URL')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

app = Flask(__name__)

@app.route("/.well-known/webfinger", methods=["GET"])
def webfinger():
    response = {
        "subject": f"acct:{ADMIN_EMAIL}",
        "links": [
            {
                "rel": "http://openid.net/specs/connect/1.0/issuer",
                "href": f"{OAUTH_SERVER_URL}"
            }
        ]
    }

    return jsonify(response)


@app.errorhandler(Exception)
def error(e):
    if isinstance(e, HTTPException):
        code = e.code
        error = e.description
    else:
        code = 500
        error = "Internal Server Error"

    return jsonify({
        "error": error,
        "requested_url": request.url,
        "method": request.method,
        "message": "Make a GET request at '/.well-known/webfinger' ",
    }), code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
