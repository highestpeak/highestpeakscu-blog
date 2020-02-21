from flask_restful import fields

articleIterResponse = {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'create_time': fields.String,
    'tags': fields.List(fields.String),
}

articleListResponse = {
    'total': fields.Integer(default=100),
    'per_page': fields.Integer(default=10),
    'start': fields.Integer(default=0),
    'list': fields.Nested(articleIterResponse)
}

articleDetailResponse = {
    'articleTitle': fields.String,
    'articleDate': fields.String,
    'articleContent': fields.String,
    'articleStars': fields.Integer(default=0),
    'articleTag': fields.List(fields.String),
}

tagHasResponse = {
    'id': fields.Integer,
    'title': fields.String,
}

tagResponse = {
    'name': fields.String,
    'list': fields.Nested(tagHasResponse),
}

# github repo
repoResponse = {
    'repoURL': fields.String,
}

timeLineSectionItemResponse = {
    "title": fields.String,
    "id": fields.Integer,
    "date": fields.String,
}
timeLineResponse = {
    'section': fields.String,
    'list': fields.Nested(timeLineSectionItemResponse),
}
