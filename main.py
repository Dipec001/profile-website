from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True)
