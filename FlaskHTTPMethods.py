from flask import Flask,request

app = Flask(__name__)
@app.route("/")
def index():
    return "meth used %s"%request.method
@app.route("/check", methods=['POST','GET'])
def check():
    if request.method=='POST':
        return "You are accessing POST"
    else:
        return "You are accessing GET"


if __name__=="__main__":
    app.run(debug=True)
