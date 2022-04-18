from sqlalchemy.orm import declarative_base, relationship, declarative_mixin
from sqlalchemy import Integer, String, Column, TIMESTAMP, ForeignKey, Text
import time
from dotenv import dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bootstrap import AppConfig
from os import path


app = Flask(__name__)
conf = dotenv_values(path.join(app.root_path, '.env'))

app.config['SQLALCHEMY_DATABASE_URI'] = conf['DATABASE_URI']
db = SQLAlchemy(app)

Base = declarative_base()


@declarative_mixin
class TimestampMixin:
    created_at = Column(Integer, default=int(time.time()))


class Post(TimestampMixin, db.Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    imgur_id = Column(String(25))
    title = Column(String(512))

    images = relationship(
            "Image", back_populates="post", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Post(id={self.id!r}, title={self.title!r})"

class Image(TimestampMixin, db.Model):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    imgur_id = Column(String(25))
    description = Column(Text)
    link = Column(String(128))
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('Post', back_populates='images')

    def __repr__(self):
        return f"Image(id={self.id!r}, description={self.description!r}, link={self.link!r})"
