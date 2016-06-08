from flask import Flask,request
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/call")
def call():
    print "call received"
    return ""

@app.route("/reset", methods=['GET'])
def reset():
    print "reset received"
    print "cause : "+request.args.get('cause')
    return ""

@app.route("/nextCommand")
def nextCommand():
    r = random.randint(0,4)
    if r == 0:
        return "NOTHING"
    if r == 1:
        return "UP"
    if r == 2:
        return "DOWN"
    if r == 3:
        return "OPEN"
    if r == 4:
        return "CLOSE"

if __name__ == "__main__":
    app.run()
