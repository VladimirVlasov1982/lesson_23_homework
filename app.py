import os

from flask import Flask, request
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        req = RequestSchema().load(dict(request.values.items()))
    except ValidationError as error:
        return error.messages, 400

    if not os.path.isfile(f'data/{req["file_name"]}'):
        return "File not found", 400
    result = build_query(req)
    return app.response_class('\n'.join(result), content_type="text/plain")


if __name__ == "__main__":
    app.run()