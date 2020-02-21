from datetime import datetime

from flask_restful import reqparse


def articleListParser():
    parser = reqparse.RequestParser()
    parser.add_argument('start', type=int)
    parser.add_argument('num', type=int)
    parser.add_argument('requirement', type=str)
    return parser


def articleDetailParser():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    return parser


def articleStarParser():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    parser.add_argument('star', type=int)
    return parser


def articleAdminParser():
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('description', type=str)
    parser.add_argument('repourl', type=str)
    parser.add_argument('star_send_num', type=str)
    parser.add_argument('stars', type=int)
    parser.add_argument('create_time', type=str)
    parser.add_argument('tags', type=str, action='append')
    parser.add_argument('hash', type=str)
    return parser


def tagAdminParser():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('description', type=str)
    parser.add_argument('create_time', type=str)
    parser.add_argument('hash', type=str)
    return parser


def repoAdminParser():
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str)
    parser.add_argument('hash', type=str)
    return parser
