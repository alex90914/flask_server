#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Config:
    # 邮件发送相关配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '343618924@qq.com'
    MAIL_PASSWORD = 'qdllxwqzyspsbijh'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # mysql配置相关
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:dream@2018.@118.25.212.23:3306/flask'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:dream@2018.@reamatach.com:3306/flask'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
