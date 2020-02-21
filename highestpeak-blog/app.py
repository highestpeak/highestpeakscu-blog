import click
from flask import Flask, render_template
from flask_cors import CORS

from db.database.model import db
from configOperate import Setting

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )

# config
settingsConfig = Setting().get()
SQLALCHEMY_DATABASE_URI = \
    "mysql://" + settingsConfig.get("mysql_username") + \
    ":" + settingsConfig.get("mysql_password") + \
    "@" + settingsConfig.get("mysql_hostname") + \
    "/" + settingsConfig.get("mysql_database")
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['SECRET_KEY'] = settingsConfig.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db init
db.init_app(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# blueprints
from API.api import article_blueprint, tag_blueprint, anything_blueprint

app.register_blueprint(article_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(anything_blueprint)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

# with app.app_context():
#     db.create_all()

# if __name__ == '__main__':
#     print("sss")
#     db.create_all()
#     app.run()

