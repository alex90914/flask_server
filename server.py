#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request
import uuid
import os

app = Flask(__name__)


@app.route("/ajax", methods=["POST"])
def ajax():
    json_data = request.data
    return json_data


@app.route("/form", methods=["POST"])
def form():
    data = request.form
    return data


@app.route("/args", methods=["POST"])
def args():
    data = request.args
    return data


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files['file']
    suffix = os.path.splitext(files.filename)[1]
    files.save("%s.%s" % (uuid.uuid1(), suffix))
    return {"msg": "上传成功"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
