from flask import Flask, render_template
from post import Post
import requests
from datetime import datetime


app = Flask(__name__)

today = datetime.today()
current_year = today.year

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def get_all_posts():
    """Renders the blog start page.
    """

    return render_template("index.html", year=current_year, all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    """Renders an individual blog post page.
    """

    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post

    return render_template("post.html", year=current_year, post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
