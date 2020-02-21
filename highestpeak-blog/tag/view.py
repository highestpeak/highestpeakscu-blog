from flask_restful import marshal_with, Resource

from API.APIKey import tagKey
from API.APIPaser import tagAdminParser
from API.APIResponse import tagResponse
from db.database.model import Tags, db


class TagApi(Resource):
    @marshal_with(tagResponse)
    def get(self):
        tagList = list(Tags.query.order_by(Tags.create_time.desc()))
        returnItem = []
        for tag in tagList:
            item = {
                'name': tag.name,
                'list': [],
            }
            for article in tag.articles:
                item["list"].append({
                    'id': article.id,
                    'title': article.title,
                })
            returnItem.append(item)
        return returnItem

    # 允许在文章外新增标签是一个错误的选择
    # def post(self):
    #     args = tagAdminParser().parse_args()
    #     if args["hash"] != tagKey():
    #         return None
    #     tag = Tags(
    #         name=args["name"],
    #         description=args["description"],
    #         create_time=args["create_time"]
    #     )
    #     db.session.add(tag)
    #     db.session.commit()
    #     return "ok"

    def put(self):
        args = tagAdminParser().parse_args()
        if args["hash"] != tagKey():
            return None
        tag = Tags.query.filter_by(name=args["name"]).first()
        if tag is None:
            tag = Tags(
                name=args["name"],
                description=args["description"],
                create_time=args["create_time"]
            )
        else:
            del args["hash"]
            for key, value in args.items():
                if value is None:
                    continue
                elif key == "name":
                    tag.name = value
                elif key == "description":
                    tag.description = value
                elif key == "create_time":
                    tag.create_time = value
        db.session.add(tag)
        db.session.commit()
        return "ok"

    def delete(self):
        args = tagAdminParser().parse_args()
        if args["hash"] != tagKey():
            return None
        tag = Tags.query.filter_by(name=args["name"]).first()
        db.session.delete(tag)
        db.session.commit()
        return "ok"
