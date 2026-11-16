#web app

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))

#def home():
#    return "Hello, World!"

if __name__ == "__main__":
    #app.run(debug=True) #if you change the code it will stop/restart automatically
    app.run()
