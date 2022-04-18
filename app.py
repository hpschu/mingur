from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from bootstrap import AppConfig
from models import Post

conf = AppConfig('.env')


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = conf.DATABASE_URI

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)
