"""Blogly application."""

from flask import Flask, redirect, request, render_template, session, flash
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

#showing home page...............
@app.route("/")
def main():
    users = User.query.all()
    return render_template('home.html', users = users)

#posting from home page..........
@app.route("/", methods = ["POST"])
def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image = request.form["image"] 

    
    new_user = User(first = first_name, last = last_name, image = image)
    db.session.add(new_user)
    db.session.commit()
    return redirect (f"/{new_user.id}")

#showing detailed info of user.....
@app.route("/<int:user_id>")
def details(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.all()
    return render_template('detail_user.html', user = user, posts = posts)

@app.route("/<int:user_id>", methods=['POST'])
def detailed(user_id):
    first_name = request.form["new_first_name"]
    last_name = request.form["new_last_name"]
    image = request.form["new_image"]

    user = User.query.get_or_404(user_id)
    user.first = first_name
    user.last = last_name
    user.image = image

    db.session.add(user)
    db.session.commit() 
    return render_template('detail_user.html', user = user)


#star of edit....................
@app.route("/<int:user_id>/edit")
def edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user = user)
   

@app.route("/<int:user_id>/edit", methods = ["POST"])
def apply_edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template ("detail_user.html", user = user)
#end of editing....................


#start of deleting.................
@app.route("/<int:user_id>/delete")
def delete(user_id):
    user = User.query.get_or_404(user_id)
    Post.query.filter(Post.user_id == user_id).delete()
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    users = User.query.all()
    return render_template('home.html', users = users)

    # going on ADD Post page
@app.route("/<int:user_id>/add_post")
def add_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('add_post.html', user = user)

@app.route("/<int:user_id>/add_post", methods = ["POST"])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("detail_post.html", user = user, post = post)



# detailed post................

@app.route("/<int:user_id>/<int:post_id>")
def detail_post_form(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template("detail_post.html", user = user, post = post)


@app.route("/<int:user_id>/detail_post", methods = ["POST"])
def detailed_post(user_id):
    user = User.query.get_or_404(user_id)

    post_title = request.form['title']
    post_content = request.form['content']
    created_at = request.form['created_at']

    post = Post(title = post_title, content = post_content, created_at = created_at, user_id = user_id)
    db.session.add(post)
    db.session.commit()
    return redirect (f"/{user.id}/{post.id}")

