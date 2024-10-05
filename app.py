from flask import Flask, render_template, abort
from jobs import jobs
from summaries import initial_summary
from blog_posts import blog_posts

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "title": "Steve Watson | CV",
        "first_name": "Steve",
        "last_name": "Watson",
        "initial_summary_text": initial_summary,
        "jobs": jobs,
    }
    return render_template('index.html', **context)

@app.route('/blog')
def blog():
    context = {
        "title": "Steve Watson | Blog",
        "blog_posts": blog_posts
    }
    return render_template('blog/blog_list.html', **context)

@app.route('/blog/<slug>')
def blog_post(slug):
    # Find the blog post with the matching slug
    blog_post = next((post for post in blog_posts if post["slug"] == slug), None)

    # If no blog post is found, return a 404 error
    if blog_post is None:
        abort(404)

    context = {
        "title": blog_post["title"],
        "blog_post": blog_post
    }
    return render_template('blog/blog_post.html', **context)

if __name__ == '__main__':
    app.run(debug=True)