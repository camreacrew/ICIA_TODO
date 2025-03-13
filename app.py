from flask import Flask, render_template
from finance_view import finance_app


app = Flask(__name__)

app.register_blueprint(finance_app)

@app.route("/")
def index():
    return render_template("index.html")


