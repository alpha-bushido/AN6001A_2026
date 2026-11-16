#web app

from flask import Flask, render_template, request
import joblib

model = joblib.load("dbs.pkl")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = request.form.get("q")
    return(render_template("dbs.html"))

@app.route("/dbsResult",methods=["GET","POST"])
def dbsResult():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    return(render_template("dbsResult.html",r=r[0][0]))

#def home():
#    return "Hello, World!"

if __name__ == "__main__":
    #app.run(debug=True) #if you change the code it will stop/restart automatically
    app.run()
