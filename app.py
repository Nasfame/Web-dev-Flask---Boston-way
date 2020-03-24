from flask import Flask, render_template as rt

app = Flask(__name__)
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return rt("user.html",user=user)

@app.route('/shopping')
def shopping():
    food = ['chesse','lettuce','milk']
    return rt("shopping.html",food=food)
if __name__=="__main__":
    app.run(debug=True)
