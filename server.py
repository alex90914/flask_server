#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import uuid
import os
from flask_config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

db = SQLAlchemy(app)


class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)


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


@app.route("/templates", methods=["GET"])
def templates():
    return render_template('demo.html', name="张三")


@app.route("/send_email")
def send_email():
    msg = Message('Hello', sender='343618924@qq.com', recipients=['343618924@qq.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return {"msg": "发送成功"}


@app.route("/add_role")
def add_role():
    db.create_all()
    return {"msg": "发送成功"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
