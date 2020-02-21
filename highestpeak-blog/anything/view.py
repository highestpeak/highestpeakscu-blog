from flask import jsonify
from flask_restful import marshal_with, Resource

from API.APIKey import repoKey
from API.APIPaser import repoAdminParser
from API.APIResponse import timeLineResponse, repoResponse
from configOperate import UiSetting
from db.database.model import Repos, Article, db


class RepoApi(Resource):
    @marshal_with(repoResponse)
    def get(self):
        repos = Repos.query.all()
        repolist = []
        for repo in repos:
            repolist.append({
                "repoURL": repo.repourl
            })
        return repolist

    def post(self):
        args = repoAdminParser().parse_args()
        if args["hash"] != repoKey():
            return None
        repo = Repos(repourl=args["url"])
        db.session.add(repo)
        db.session.commit()
        return "ok"

    def put(self):
        args = repoAdminParser().parse_args()
        if args["hash"] != repoKey():
            return None
        repo = Repos.query.filter_by(repourl=args["repourl"]).first()
        if repo is None:
            repo = Repos(repourl=args["repourl"])
        else:
            repo.repourl = args["repourl"]
        db.session.add(repo)
        db.session.commit()
        return "ok"

    def delete(self):
        args = repoAdminParser().parse_args()
        if args["hash"] != repoKey():
            return None
        repo = Repos.query.filter_by(repourl=args["url"]).first()
        db.session.delete(repo)
        db.session.commit()
        return "ok"


class TimeLineApi(Resource):
    @marshal_with(timeLineResponse)
    def get(self):
        articleList = list(Article.query.order_by(Article.create_time.desc()))
        timeLine = {}
        for article in articleList:
            create_time = article.create_time
            section = create_time.__format__('%Y-%m')
            if section is not None and section not in timeLine.keys():
                timeLine[section] = []
            timeLine[section].append({
                "title": article.title,
                "id": article.id,
                "date": create_time.__format__('%Y-%m-%d %A %H:%M:%S'),
            })
        timeLineList = []
        for key, value in timeLine.items():
            timeLineList.append({
                "section": key,
                "list": value,
            })
        return timeLineList


class SettingApi(Resource):
    def get(self):
        return jsonify(UiSetting.get())
