from flask import Flask,render_template

app = Flask(__name__)


@app.route("/magzine")
def magzine():
    return render_template("magzine.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/yoro")
def yoro():
    return render_template("yoro.html")

if __name__ == "__main__":
    app.run(debug=True)

