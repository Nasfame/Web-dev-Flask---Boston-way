app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/Bye')
def tuna():
    return "Gud Bye"
@app.route('/profiles/user')
def profile(user):
    return user
@app.route('/post/<int:postid>')
def show(postid):
    return "%s" %postid


if __name__ == '__main__':
    app.run()


