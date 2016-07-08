from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for('user', username=username))
    return redirect(url_for('index'))


@app.route("/user/")
@app.route("/user/<username>")
def user(username=None):
    if not username:
        return redirect(url_for('index'))
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(
        debug=True
    )
