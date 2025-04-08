from flask import Flask, render_template

app = Flask(__name__)


@app.route('/scan')
@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8668)
