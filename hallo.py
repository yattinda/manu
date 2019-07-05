
# hello.py

from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello_world():
	return"Hello world"

if _name_ == "_main_":
	app.run()
