from flask import Blueprint
from flask_restful import Api

from anything.view import TimeLineApi, RepoApi, SettingApi
from article.view import ArticlesApi, ArticleApi, StarApi, ArticleNumApi
from tag.view import TagApi

article_blueprint = Blueprint("article", __name__)
tag_blueprint = Blueprint("tag", __name__)
anything_blueprint = Blueprint("anything", __name__)

article_api = Api(article_blueprint)
tag_api = Api(tag_blueprint)
anything_api = Api(anything_blueprint)

article_api.add_resource(ArticleNumApi, "/api/articlenums")
article_api.add_resource(ArticlesApi, "/api/articles")
article_api.add_resource(ArticleApi, "/api/article")
article_api.add_resource(StarApi, "/api/star")

tag_api.add_resource(TagApi, "/api/tags")

anything_api.add_resource(RepoApi, "/api/repo")
anything_api.add_resource(TimeLineApi, "/api/timeline")
anything_api.add_resource(SettingApi, "/api/setting")
