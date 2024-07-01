from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

username = "Tomdu3"
description = "I love developing web applications."
description += "And this text was created with Jinja"


@app.route('/')
def hello_world():
    return render_template('index.html', username = username, description = description)

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        return 'You are using POST'
    elif request.method == 'GET':
        return 'You are using GET'


if __name__ == '__main__':
    app.run()