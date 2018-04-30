from flask import render_template
from app import app

@app.route("/")
@app.route("/login")
def login():
	return "Hello, World!"
