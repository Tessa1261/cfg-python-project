# mandatory import the library
from flask import Flask, render_template

# create an index route
app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return render_template("index.html")

#app runs!
app.run(debug=True)
