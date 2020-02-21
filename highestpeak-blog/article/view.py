from datetime import datetime

from flask import jsonify
from flask_restful import marshal_with, Resource

from API.APIKey import articleKey
from API.APIPaser import articleListParser, articleDetailParser, articleAdminParser, articleStarParser
from API.APIResponse import articleListResponse, articleDetailResponse
from db.database.model import Article, db, Tags, article_tags


class ArticleNumApi(Resource):
    def get(self):
        returnItem = {
            'total': Article.query.count(),
        }
        return jsonify(returnItem)

class ArticlesApi(Resource):

    # 查
    @marshal_with(articleListResponse)
    def get(self):
        args = articleListParser().parse_args()
        if args is None:
            return None

        # todo: get article by requirement
        # requirement = args['requirement']
        # if isinstance(requirement, str):
        #     requirement = eval(requirement)

        start = args['start']
        num = args['num']
        # articleList = Article.query.order_by(Article.create_time).reverse()[start:end]
        articleList = list(Article.query.order_by(Article.create_time.desc()).offset(start).limit(num))
        returnItem = {
            'total': Article.query.count(),
            'start': start,
            'list': [],
        }
        for article in articleList:
            item = {
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'create_time': article.create_time,
                'tags': [],
            }
            for tag in article.tags:
                item["tags"].append(tag.name)
            returnItem["list"].append(item)
        return returnItem


class ArticleApi(Resource):

    def addArticle(self, args):
        article = Article(
            title=args["title"],
            description=args["description"],
            content=args["repourl"],
            star_send_num=args["star_send_num"] if args["star_send_num"] is not None else 0,
            stars=args["stars"] if args["stars"] is not None else 0,
            create_time=args["create_time"],
        )

        for tag in args["tags"]:
            tagDB = Tags.query.filter_by(name=tag).first()
            if tagDB is None:
                tagDB = Tags(name=tag)
            article.tags.append(tagDB)

        db.session.add(article)
        db.session.commit()

    # 增
    def post(self):
        args = articleAdminParser().parse_args()
        if args["hash"] != articleKey():
            return None
        args["create_time"] = datetime.strptime(args["create_time"], "%Y-%m-%d %H:%M:%S")
        self.addArticle(args)
        return "ok"

    # 删
    def delete(self):
        args = articleAdminParser().parse_args()
        if args["hash"] != articleKey():
            return None
        article = Article.query.filter_by(title=args["title"]).first()
        db.session.delete(article)
        db.session.commit()
        return "ok"

    # 改
    def put(self):
        args = articleAdminParser().parse_args()
        if args["hash"] != articleKey():
            return None
        article = Article.query.filter_by(title=args["title"]).first()
        if article is None:
            self.addArticle(args)
        else:
            del args["hash"]
            for key, value in args.items():
                if value is None:
                    continue
                elif key == "title":
                    article.title = value
                elif key == "description":
                    article.description = value
                elif key == "repourl":
                    article.repourl = value
                elif key == "star_send_num":
                    article.star_send_num = value
                elif key == "stars":
                    article.stars = value
                elif key == "create_time":
                    article.create_time = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                elif key == "tags":
                    article.tags = []
                    for tag in args["tags"]:
                        tagDB = Tags.query.filter_by(name=tag).first()
                        if tagDB is None:
                            tagDB = Tags(name=tag)
                        article.tags.append(tagDB)
            db.session.add(article)
            db.session.commit()
        return "ok"

    # 查
    @marshal_with(articleDetailResponse)
    def get(self):
        args = articleDetailParser().parse_args()
        if args is None:
            return None
        articleDB = Article.query.filter_by(id=args["id"]).first()
        articleReturn = {
            'articleTitle': articleDB.title,
            'articleDate': articleDB.create_time,
            'articleContent': articleDB.content,
            'articleStars': articleDB.stars,
            'articleTag': [],
        }
        for tag in articleDB.tags:
            articleReturn["articleTag"].append(tag.name)
        return articleReturn


class StarApi(Resource):
    def put(self):
        args = articleStarParser().parse_args()
        if args is None:
            return None
        articleDB = Article.query.filter_by(id=args["id"]).first()
        if articleDB is None:
            return None
        else:
            totalNum = articleDB.star_send_num * articleDB.stars + args["star"]
            articleDB.star_send_num += 1
            articleDB.stars = round(totalNum / articleDB.star_send_num, 2)
            db.session.add(articleDB)
            db.session.commit()
