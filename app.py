from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "ola"


app.run(debug=True)