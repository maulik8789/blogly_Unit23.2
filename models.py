from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Blogly."""

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id= {u.id} first_name = {u.first_name} last = {u.last_name} image = {u.image}>"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)

    first = db.Column(db.String(30),
                      nullable = False)

    last = db.Column(db.String(30),
                      nullable = False)

    image = db.Column(db.String)

    def greet(self):
        return f"Hello, I am {u.first}"

class Post(db.Model):
    __tablename__ = "posts"

    def __repr__(self):
        p = self
        return f"<Post id= {p.id} title = {p.title} content = {p.content} created_at = {p.created_at} user_id = 'users.id'>"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)

    title = db.Column(db.String(999),
                      nullable = False)

    content = db.Column(db.String(9999),
                      nullable = False)

    created_at = db.Column(db.DateTime(timezone=True),
                      nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
