# mandatory import the library
from flask import Flask

# create an index route
app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return"hello world!"

#app runs!
app.run(debug=True)
