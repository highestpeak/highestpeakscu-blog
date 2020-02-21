from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# article_tags 联系表
article_tags = \
    db.Table('article_tags',
             db.Column('id', db.Integer, primary_key=True),
             db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
             db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
             )


# 分类
class Tags(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.CHAR(16), nullable=False, unique=True)
    description = db.Column(db.Text,default="")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<Tags %r>' % self.name


# 文章
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.CHAR(36), nullable=False, unique=True)
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    star_send_num = db.Column(db.Integer, default=0)
    stars = db.Column(db.FLOAT, default=0)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # article_tags 联系表 多对多
    tags = db.relationship('Tags', secondary=article_tags, lazy='subquery',
                           backref=db.backref('articles', lazy=True))

    def __repr__(self):
        return '<Article %r>' % self.title


# 仓库
class Repos(db.Model):
    __tablename__ = 'repo'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    repourl = db.Column(db.Text)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<Repos %r>' % self.name
