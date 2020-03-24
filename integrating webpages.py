from flask import Flask,render_template

app = Flask(__name__)
@app.route("/profile/<name>")
def index(name):
    return render_template("profile.html",name=name)


'''Cooler way but no recommended'''

@app.route("/Cool/<name>")
def cool(name):
	return "<h2> Hi %s"%name




if __name__=="__main__":
    app.run(debug=True)
