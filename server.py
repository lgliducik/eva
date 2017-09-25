import sys
import os
import logging

from flask import Flask, request


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    logger.info("request processing")
    if request.method == "GET":
        return "Hello"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    app.run(port=int(os.environ.get("PORT", 5000)))
