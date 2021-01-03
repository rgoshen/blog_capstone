from flask import Flask, render_template
import requests
from datetime import datetime


app = Flask(__name__)

today = datetime.today()


@app.route('/')
def home():
    """Renders the blog start page.
    """

    current_year = today.year

    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    resp = requests.get(blog_url)
    all_posts = resp.json()
    return render_template("index.html", year=current_year, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
