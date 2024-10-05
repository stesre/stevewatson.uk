from flask import Flask, render_template, abort, request
from jobs import jobs
from summaries import initial_summary
from blog_posts import blog_posts
from utils.helper import is_valid_signature
import git, os

github_webhook_secret = os.environ['GITHUB_WEBHOOK_SECRET']
app = Flask(__name__)

@app.route('/update_from_github', methods=['POST'])
def webhook():
    if request.method == 'POST':
        x_hub_signature = request.headers.get('X-Hub-Signature')
        # webhook content type should be application/json for request.data to have the payload
        # request.data is empty in case of x-www-form-urlencoded
        if not is_valid_signature(x_hub_signature, request.data, github_webhook_secret):
            print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
            abort("Invalid secret from GitHub")
        repo = git.Repo('mysite/stevewatson.uk', search_parent_directories=True)
        repo.head.reset(index=True, working_tree=True)
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

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