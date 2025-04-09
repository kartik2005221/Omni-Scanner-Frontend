import platform

from flask import Flask, render_template

from utils.administrative_utils import is_sudo_linux

app = Flask(__name__)


@app.route('/scan')
@app.route('/')
def home():
    """Home page route"""
    if platform.system() == "Linux":
        sudo_status = is_sudo_linux()
    else:
        sudo_status = None
    return render_template('index.html', sudo_status=sudo_status)


@app.route('/switch_sudo')
def switch_sudo():
    """Switch Sudo page route"""
    if platform.system() == "Linux":
        sudo_status = is_sudo_linux()
    else:
        sudo_status = None
    return render_template('switch_sudo.html', sudo_status=sudo_status)


@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.route('/history')
def history():
    """History page route"""
    return render_template('history.html')


@app.route('/cli')
def cli():
    """CLI page route"""
    return render_template('cli.html')




@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8668)
