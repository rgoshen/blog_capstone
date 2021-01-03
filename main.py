from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    resp = requests.get(blog_url)
    all_posts = resp.json()
    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
